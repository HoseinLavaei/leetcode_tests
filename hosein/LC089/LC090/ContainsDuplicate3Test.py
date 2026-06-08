from .ContainsDuplicate3 import Solution

def test_contains_duplicates():
    assert Solution().containsNearbyAlmostDuplicate(nums = [1,2,3,1], indexDiff = 3, valueDiff = 0) == True