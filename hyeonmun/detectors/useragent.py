import re

SUSPICIOUS_KEYWORDS = [
    "sqlmap", "curl", "wget", "python", "aiohttp", 
    "mechanize", "phantomjs", "scrapy", "bot", "spider", "Headless"
]

def check_ua(ua: str) -> bool:
    """Check if User-Agent looks suspicious (rule-based)"""
    if not ua or ua.strip() == "":
        return True  # Empty UA is suspicious
    
    ua_lower = ua.lower()
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in ua_lower:
            return True
    return False
