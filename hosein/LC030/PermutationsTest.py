from .Permutations import Solution

def test_permutations():
    assert Solution().permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
