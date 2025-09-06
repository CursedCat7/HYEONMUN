from datetime import datetime, timedelta
import threading


_js_pings = {}
_lock = threading.Lock() 

def register_js_ping(ip: str):
    """Register JS ping"""
    now = datetime.utcnow()
    with _lock:
        _js_pings[ip] = now
        _cleanup(timeout=60)

def check_js_active(ip: str, timeout: int = 60) -> bool:
    """Return False if JS inactive"""
    now = datetime.utcnow()
    with _lock:
        last_ping = _js_pings.get(ip)
        if not last_ping:
            return False
        active = (now - last_ping) < timedelta(seconds=timeout)
        if not active:
            del _js_pings[ip]
        return active

def _cleanup(timeout: int):
    """Remove stale IP entries"""
    now = datetime.utcnow()
    stale_ips = [ip for ip, ts in _js_pings.items() if (now - ts) > timedelta(seconds=timeout)]
    for ip in stale_ips:
        del _js_pings[ip]
