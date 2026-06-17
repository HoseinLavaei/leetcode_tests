import os
import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

def _decode(obj):
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    if isinstance(obj, dict):
        return {str(_decode(k)): _decode(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_decode(item) for item in obj]
    return obj

def run_lua_script(script_path, capture_output=False):
    with open(script_path, 'r') as f:
        lua_script = f.read()
    r = redis.Redis.from_url(REDIS_URL)
    result = r.eval(lua_script, 0)
    return _decode(result) if capture_output else None

def run_redis_test(base_dir):
    r = redis.Redis.from_url(REDIS_URL)
    run_lua_script(os.path.join(base_dir, "setup.lua"), capture_output=False)
    result = run_lua_script(os.path.join(base_dir, "test.lua"), capture_output=True)
    r.close()
    return result