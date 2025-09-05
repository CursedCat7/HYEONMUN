import json

def log_event(ip: str, results: dict, score: int):
    """Log IP event with risk score"""
    log = {"ip": ip, "results": results, "risk_score": score}
    print("[HYEONMUN LOG]", json.dumps(log, ensure_ascii=False))