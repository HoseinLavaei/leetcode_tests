import os
import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")


def _decode(obj):
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    if isinstance(obj, dict):
        return {str(_decode(k)): _decode(v) for k, v in obj.items()}   # <-- cast key to str
    if isinstance(obj, (list, tuple)):
        return [_decode(item) for item in obj]
    return obj


def run_redis_test(setup_function, test_function):
    r = redis.Redis.from_url(REDIS_URL)
    setup_function(r)
    result = test_function(r)
    r.close()
    return _decode(result)