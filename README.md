# HYEONMUN
Hyeonmun(玄門) : Abnormal Network Traffic Gate FastAPI Moudle Project 
⸻


# Hyeonmun (賢門)

**Abnormal Network Traffic Gate FastAPI Module Project**  
Hyeonmun is a logging and tagging-focused security gateway module for FastAPI applications.  
It detects VPNs, Tor nodes, anonymous proxies, and abnormal network traffic, helping administrators monitor and analyze client requests in real time.

## Key Features

- Tor Exit Node detection
- VPN / Anonymous Proxy / Data Center IP detection
- ASN / WHOIS-based cloud and hosting IP identification
- External reputation DB integration (e.g., AbuseIPDB)
- Behavior-based abnormal traffic detection (port scanning, high request rate)
- User-Agent analysis (headless browsers, bots)
- Risk scoring and logging
- Redis caching and Postgres/ClickHouse event logging support
- Easy integration as FastAPI middleware

## Installation

```
pip install hyeonmun
```

FastAPI Integration Example
```
from fastapi import FastAPI
from hyeonmun.middleware import IPReputationMiddleware

app = FastAPI()
app.add_middleware(IPReputationMiddleware)

@app.get("/")
async def root(request):
    return {
        "msg": "Welcome to Hyeonmun (賢門)",
        "ip_info": request.state.ip_reputation
    }
```
Development & Contribution
	•	hyeonmun/detectors/ – Detection modules (Tor, VPN, Proxy, ASN, User-Agent, behavior)
	•	hyeonmun/scoring/ – Risk scoring engine
	•	hyeonmun/storage/ – Cache and database integration
	•	hyeonmun/tasks/ – Background tasks for DB updates and external API enrichment
	•	tests/ – Unit and integration tests

Project Goal

Hyeonmun is designed primarily for logging and tagging rather than blocking.
It allows administrators to observe and analyze incoming traffic in real time, identify risky IPs, and make informed security decisions.

License

This project is licensed under the MIT License. See the LICENSE file for details.
