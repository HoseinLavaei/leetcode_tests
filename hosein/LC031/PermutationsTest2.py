from .Permutations2 import Solution

def test_permutations_2():
    assert sorted(Solution().permuteUnique([1,1,2])) == sorted([[1,1,2],[1,2,1],[2,1,1]])
