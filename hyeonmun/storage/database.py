import json
import os
from datetime import datetime

LOG_FILE = "/logs/hyeonmun_log.jsonl"

class Database:
    def save_log(self, data: dict):
        try:
            with open(LOG_FILE, "a") as f:
                log_entry = {
                    "client_ip": data.get("client_ip"),
                    "risk_score": data.get("risk_score"),
                    "results": data.get("results"),
                    "timestamp": datetime.utcnow().isoformat()
                }
                f.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Error saving log to file: {e}")

def create_db_and_tables():
    pass


