from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        the_array = list(set(sorted(nums1+nums2)))
        if len(the_array)%2==0:
            return (the_array[len(the_array)//2 - 1] + the_array[len(the_array)//2])/2
        return the_array[len(the_array)//2]
