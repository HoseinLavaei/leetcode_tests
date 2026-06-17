import os
from hosein.run_redis_test import run_redis_test

def test_rate_limiter():
    assert run_redis_test(os.path.dirname(__file__)) == 6