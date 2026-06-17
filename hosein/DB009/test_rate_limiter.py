from .setup import run_setup
from .test import run_test
from hosein.run_redis_test import run_redis_test

def test_rate_limiter():
    assert run_redis_test(run_setup, run_test) == 6