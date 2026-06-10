from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        highest_volume = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            volume = width * h
            highest_volume = max(highest_volume, volume)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return highest_volume