from urllib.parse import urlparse, parse_qs

SUSPICIOUS_PATTERNS = ["'", "\"", "--", ";", "/*", "*/"]

async def check_params(request) -> bool:
    """Return True if suspicious query or body"""
    query_params = parse_qs(urlparse(str(request.url)).query)
    for values in query_params.values():
        for v in values:
            for pattern in SUSPICIOUS_PATTERNS:
                if pattern in v:
                    return True
    try:
        json_data = await request.json()
        for v in json_data.values():
            if isinstance(v, str):
                for pattern in SUSPICIOUS_PATTERNS:
                    if pattern in v:
                        return True
    except:
        pass
    return False
