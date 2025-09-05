def calculate_risk_score(results: dict) -> int:
    """Calculate risk score based on rules (0~100)"""
    score = 0
    if results.get("tor"): score += 40
    if results.get("vpn_proxy"): score += 30
    if results.get("useragent"): score += 20
    if results.get("behavior"): score += 50
    if results.get("referer"): score += 25
    return min(score, 100)