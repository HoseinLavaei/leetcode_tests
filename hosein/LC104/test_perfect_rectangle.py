from .perfect_rectangle import Solution

def test_perfect_rectangle():
    assert Solution().isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]) == True