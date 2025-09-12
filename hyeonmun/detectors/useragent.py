import re

SUSPICIOUS_KEYWORDS = [
    "sqlmap", "curl", "wget", "python", "aiohttp", 
    "mechanize", "phantomjs", "scrapy", "bot", "spider", "Headless",
    "headlesschrome", "puppeteer", "mediapartners-google", "adsbot",
    "bingbot", "slurp", "duckduckbot", "baiduspider", "yandexbot",
    "semrushbot", "ahrefsbot", "mj12bot", "dotbot", "petalbot",
    "screaming frog", "python-requests", "go-http-client"
]

def check_ua(ua: str) -> bool:
    """Check if User-Agent looks suspicious (rule-based)"""
    if not ua or ua.strip() == "":
        return True  # Empty UA is suspicious
    
    ua_lower = ua.lower()
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in ua_lower:
            return True
            
    if len(ua) < 20:
        return True
        
    return False


