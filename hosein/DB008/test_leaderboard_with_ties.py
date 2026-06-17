import os
from hosein.run_redis_test import run_redis_test

def test_leaderboard_with_ties():
    assert sorted(run_redis_test(os.path.dirname(__file__))) == sorted([
        ["Bob", 1500],
        ["Dave", 1500],
        ["Carol", 1200],
        ["Alice", 1000]
    ])