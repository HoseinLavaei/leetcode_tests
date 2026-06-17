from hosein.run_redis_test import run_redis_test
from .setup import run_setup
from .test import run_test

def test_counter():
    assert run_redis_test(run_setup, run_test) == {"counter:1": 10, "counter:2": 20, "counter:3": 30}