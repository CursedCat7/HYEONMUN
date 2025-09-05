from fastapi import FastAPI, Request
from hyeonmun.middleware import IPReputationMiddleware

app = FastAPI()
app.add_middleware(IPReputationMiddleware)

@app.get("/")
async def root(request: Request):
    return {
        "msg": "Welcome to Hyeonmun (賢門)",
        "ip_info": request.state.ip_reputation,
    }