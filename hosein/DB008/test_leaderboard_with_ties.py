from .setup import run_setup
from .test import run_test
from hosein.run_redis_test import run_redis_test

def test_leaderboard_with_ties():
    assert sorted(run_redis_test(run_setup, run_test)) == sorted([
        ["Bob", 1500],
        ["Dave", 1500],
        ["Carol", 1200],
        ["Alice", 1000]
    ])