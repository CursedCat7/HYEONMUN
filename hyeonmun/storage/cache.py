import redis.asyncio as aioredis  

_rds = None

async def init_redis(uri="redis://localhost"):
    global _rds
    _rds = aioredis.from_url(uri, decode_responses=True)  

async def set_cache(key: str, value, expire: int = 60):
    if _rds is None:
        raise RuntimeError("Redis not initialized. Call init_redis() first.")
    await _rds.set(key, value, ex=expire)

async def get_cache(key: str):
    if _rds is None:
        raise RuntimeError("Redis not initialized. Call init_redis() first.")
    val = await _rds.get(key)
    return val  
