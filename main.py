from fastapi import FastAPI, Request
from hyeonmun.middleware import IPReputationMiddleware
from hyeonmun.detectors import js_check

app = FastAPI()
app.add_middleware(IPReputationMiddleware)

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
