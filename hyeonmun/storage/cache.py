import aioredis

redis = None

async def init_redis(uri="redis://localhost"):
    global redis
    redis = await aioredis.from_url(uri)

async def set_cache(key: str, value, expire: int = 60):
    await redis.set(key, str(value), ex=expire)

async def get_cache(key: str):
    val = await redis.get(key)
    if val:
        return val.decode()
    return None
