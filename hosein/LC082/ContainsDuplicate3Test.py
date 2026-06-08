from .ContainsDuplicate3 import Solution

def test_contains_duplicates_3():
    assert Solution().containsNearbyAlmostDuplicate(nums = [1,2,3,1], indexDiff = 3, valueDiff = 0) == True