import os
from hosein.run_redis_test import run_redis_test

def test_counter():
    assert {item[0]: item[1] for item in run_redis_test(os.path.dirname(__file__))} == {"counter:1": 10, "counter:2": 20, "counter:3": 30}