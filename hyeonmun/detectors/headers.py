COMMON_HEADERS = [
    "user-agent", "accept", "accept-language", "host", "connection"
]

SUSPICIOUS_HEADERS = [
    "x-forwarded-for", "via", "proxy-connection", "x-requested-with",
    "cf-connecting-ip", "true-client-ip", "x-real-ip"
]

def check_headers(request_headers: dict) -> bool:
    """Return True if headers are abnormal or suspicious"""
    headers_lower = {k.lower(): v for k, v in request_headers.items()}

    # 1. Missing common headers
    for header in COMMON_HEADERS:
        if header not in headers_lower:
            return True

    # 2. Suspicious headers indicating proxy/VPN or attack tools
    for header in SUSPICIOUS_HEADERS:
        if header in headers_lower:
            return True

    # 3. User-Agent check (already in useragent.py, but a basic check here is good)
    ua = headers_lower.get("user-agent", "")
    if not ua or len(ua) < 10: # 
        return True

    # 4. Accept-Language consistency (simple check)
    accept_language = headers_lower.get("accept-language", "")
    if accept_language and not any(lang in ua.lower() for lang in accept_language.split(',')):

        pass 

    # 5. Connection header check for HTTP/1.0 without 'keep-alive'
    connection = headers_lower.get("connection", "")
    if headers_lower.get("via") and "http/1.0" in headers_lower.get("via").lower() and "keep-alive" not in connection.lower():
        return True

    return False
