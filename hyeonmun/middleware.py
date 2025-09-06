from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from .detectors import (
    tor, vpn_proxy, useragent, behavior, referer,
    headers, params, js_check
)
from .scoring.engine import calculate_risk_score
from .storage import cache
from .utils import logging
import httpx

class IPReputationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        request_headers = request.headers
        user_agent = request_headers.get("user-agent", "")
        referrer = request_headers.get("referer", "")

        # JS ping check
        js_active = js_check.check_js_active(client_ip)

        # DoS / Rate limit check
        if behavior.check_request_rate(client_ip):
            results = {"risk_score": 100, "reason": "Rate limit exceeded"}
            response = await call_next(request)
            return response

        # Detector results
        results = {
            "tor": tor.check_ip(client_ip),
            "vpn_proxy": vpn_proxy.check_ip(client_ip),
            "useragent": useragent.check_ua(user_agent),
            "behavior": behavior.check_request_rate(client_ip),
            "referer": referer.check_referer(referrer),
            "header_change": headers.check_headers(request_headers),
            "param_tamper": await params.check_params(request),
            "js_disabled": not js_active
        }

        # Sumunjang ML integration
        ml_score = 0.0
        try:
            async with httpx.AsyncClient() as client:
                payload = {
                    "ip": client_ip,
                    "ua": user_agent,
                    "referer": referrer
                }
                r = await client.post("http://sumunjang:8000/predict/traffic", json=payload, timeout=2)
                ml_score = r.json().get("score", 0.0)
        except:
            ml_score = 0.0

        # Calculate risk score combining rule + ML
        risk_score = calculate_risk_score(results) + int(ml_score * 50)  # ML weight 0~50
        risk_score = min(risk_score, 100)

        # Redis cache
        try:
            await cache.set_cache(f"risk:{client_ip}", risk_score, expire=300)
        except Exception:
            pass

        # Logging
        logging.log_event({
            "client_ip": client_ip,
            "results": results,
            "risk_score": risk_score
        })

        request.state.ip_reputation = {
            "client_ip": client_ip,
            "results": results,
            "ml_score": ml_score,
            "risk_score": risk_score
        }

        response = await call_next(request)
        return response
