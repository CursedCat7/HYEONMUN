import redis.asyncio as aioredis  

_rds = None

async def init_redis(uri="redis://localhost"):
    global _rds
    _rds = aioredis.from_url(uri, decode_responses=True)  

async def set_cache(key, value, expire=None):
    if _rds is None:
        # Skip if Redis not initialized
        return
    try:
        await _rds.set(key, value, ex=expire)
    except Exception:
        # Ignore Redis write errors
        pass

async def get_cache(key: str):
    if _rds is None:
        # Return None if Redis not initialized
        return None
    try:
        val = await _rds.get(key)
        return val
    except Exception:
        return None
