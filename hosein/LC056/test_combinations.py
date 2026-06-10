from .combinations import Solution

def test_combinations():
    assert Solution().combine(4,2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]