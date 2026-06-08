from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        buckets = {}
        width = valueDiff + 1
        
        for i, n in enumerate(nums):
            m = n // width
            
            if m in buckets:
                return True
            if (m - 1) in buckets and abs(n - buckets[m - 1]) < width:
                return True
            if (m + 1) in buckets and abs(n - buckets[m + 1]) < width:
                return True
            
            buckets[m] = n
            
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // width]
                
        return False

