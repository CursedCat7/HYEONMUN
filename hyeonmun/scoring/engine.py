def calculate_risk_score(results: dict) -> int:
    score = 0
    if results.get("tor"): score += 40
    if results.get("vpn_proxy"): score += 30
    if results.get("useragent"): score += 20
    if results.get("behavior"): score += 50
    if results.get("referer"): score += 25
    if results.get("header_change"): score += 15          
    if results.get("param_tamper"): score += 30           
    if results.get("js_disabled"): score += 10            
    return min(score, 100)
