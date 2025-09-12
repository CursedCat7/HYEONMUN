import re

SUSPICIOUS_REFERER_DOMAINS = [
    "trafficbot.life", "free-share-buttons.com", "seo-platform.com",
    "semalt.com", "darodar.com", "priceg.com", "blackhat.com"
]

def check_referer(referer: str, allowed_domains: list = None) -> bool:
    """Detect suspicious Referer sources"""
    if not referer or referer.strip() == "":
        return True  

    referer_lower = referer.lower()


    for domain in SUSPICIOUS_REFERER_DOMAINS:
        if domain in referer_lower:
            return True


    if allowed_domains:
        is_allowed = False
        for domain in allowed_domains:
            if domain in referer_lower:
                is_allowed = True
                break
        if not is_allowed:
            return True 


    if re.match(r"^https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(:\d+)?/", referer_lower):
        return True

    return False


