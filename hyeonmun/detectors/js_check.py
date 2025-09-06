from datetime import datetime, timedelta

_js_pings = {}

def register_js_ping(ip: str):
    """Register JS ping"""
    _js_pings[ip] = datetime.utcnow()

def check_js_active(ip: str, timeout: int = 60) -> bool:
    """Return False if JS inactive"""
    last_ping = _js_pings.get(ip)
    if not last_ping:
        return False
    return (datetime.utcnow() - last_ping) < timedelta(seconds=timeout)
