# Simple in-memory cache fa
_cache = {}

class Cache:
    @staticmethod
    async def set(key: str, value: dict):
        _cache[key] = value

    @staticmethod
    async def get(key: str):
        return _cache.get(key)