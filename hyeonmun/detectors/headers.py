COMMON_HEADERS = ["user-agent", "referer", "accept", "accept-language", "host"]

def check_headers(request_headers: dict) -> bool:
    """Return True if headers abnormal"""
    for header in COMMON_HEADERS:
        if header not in request_headers:
            return True
    ua = request_headers.get("user-agent", "")
    if not ua or len(ua) < 5:
        return True
    return False
