from .CombinationSum2 import Solution

def test_combination_sum_2():
    assert sorted(Solution().combinationSum2([10,1,2,7,6,1,5], 8)) == sorted([[1,1,6],[1,2,5],[1,7],[2,6]])