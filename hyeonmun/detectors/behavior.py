from collections import defaultdict
import time

_request_log = defaultdict(list)

def check_request_rate(ip: str, limit: int = 20, interval: int = 10) -> bool:
    """Detect high request rate (basic DoS detection)"""
    now = time.time()
    _request_log[ip] = [t for t in _request_log[ip] if now - t < interval]
    _request_log[ip].append(now)
    return len(_request_log[ip]) > limit
