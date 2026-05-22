from .CombinationSum import Solution

def test_combination_sum():
    assert sorted(Solution().combinationSum([2,3,6,7], 7)) == sorted([[2,2,3],[7]])