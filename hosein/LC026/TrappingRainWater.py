from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        for left_wall in range(len(height) - 1):
            if height[left_wall] <= height[left_wall + 1]:
                continue

            filled_until_height = height[left_wall + 1]

            for right_wall in range(left_wall + 2, len(height)):
                waterline_height = min(height[left_wall], height[right_wall])
                if waterline_height <= filled_until_height:
                    continue

                width = right_wall - left_wall - 1
                water += (waterline_height - filled_until_height) * width
                filled_until_height = waterline_height

                if filled_until_height == height[left_wall]:
                    break

        return water
