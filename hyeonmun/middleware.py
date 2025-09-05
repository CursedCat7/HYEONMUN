from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from .detectors import tor, vpn_proxy, useragent, behavior, referer
from .scoring.engine import calculate_risk_score
from .storage.cache import Cache
from .utils.logging import log_event

class IPReputationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        user_agent = request.headers.get("user-agent", "")
        referrer = request.headers.get("referer", "")

        # Run rule-based detectors
        results = {
            "tor": tor.check_ip(client_ip),
            "vpn_proxy": vpn_proxy.check_ip(client_ip),
            "useragent": useragent.check_ua(user_agent),
            "behavior": behavior.check_request_rate(client_ip),
            "referer": referer.check_referer(referrer),
        }

        # Calculate risk score
        risk_score = calculate_risk_score(results)

        # Cache & log
        await Cache.set(client_ip, {"results": results, "risk_score": risk_score})
        log_event(client_ip, results, risk_score)

        # Save to request.state for API access
        request.state.ip_reputation = {
            "client_ip": client_ip,
            "user_agent": user_agent,
            "referer": referrer,
            "results": results,
            "risk_score": risk_score,
        }

        response = await call_next(request)
        return response