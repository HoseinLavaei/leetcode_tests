from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        increasing_bars: List[tuple[int, int]] = []

        for current_index, current_height in enumerate(heights):
            start_index = current_index

            while increasing_bars and increasing_bars[-1][1] > current_height:
                previous_start_index, previous_height = increasing_bars.pop()
                max_area = max(max_area, previous_height * (current_index - previous_start_index))
                start_index = previous_start_index

            increasing_bars.append((start_index, current_height))

        total_bars = len(heights)
        for start_index, height in increasing_bars:
            max_area = max(max_area, height * (total_bars - start_index))

        return max_area
