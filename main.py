from fastapi import FastAPI, Request
from hyeonmun.middleware import IPReputationMiddleware
from hyeonmun.detectors import js_check
from hyeonmun.storage.cache import init_redis
from hyeonmun.storage.database import create_db_and_tables
import uvicorn
import os

app = FastAPI()
app.add_middleware(IPReputationMiddleware)

@app.on_event("startup")
async def startup_event():
    # Redis init
    redis_uri = os.getenv("REDIS_URI", "redis://localhost")
    await init_redis(redis_uri)
    # DB later
    create_db_and_tables()

@app.get("/")
async def root(request: Request):
    """Return IP reputation results"""
    return request.state.ip_reputation

@app.get("/ping")
async def ping(request: Request):
    """Register JS ping"""
    client_ip = request.client.host
    js_check.register_js_ping(client_ip)
    return {"status": "ok"}

@app.get("/test-header")
async def test_header(request: Request):
    """Test header changes"""
    return {"headers": dict(request.headers)}

@app.get("/test-param")
async def test_param(q: str = None):
    """Test param tampering"""
    return {"query": q}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


