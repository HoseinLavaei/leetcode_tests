from .EditDistance import Solution

def test_edit_distance():
    assert Solution().minDistance("horse","ros") == 3
