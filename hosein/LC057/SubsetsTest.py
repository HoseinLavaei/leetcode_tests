from .Subsets import Solution

def test_subsets():
    assert sorted(Solution().subsets([1,2,3])) == sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])