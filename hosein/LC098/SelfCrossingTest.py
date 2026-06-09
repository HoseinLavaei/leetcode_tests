from .SelfCrossing import Solution

def test_self_crossing():
    assert Solution().isSelfCrossing([2,1,1,2]) == True