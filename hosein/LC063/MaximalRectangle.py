from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def largest_rectangle_area(heights: List[int]) -> int:
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

        column_count = len(matrix[0])
        heights = [0] * column_count
        max_rectangle = 0

        for row in matrix:
            for column_index in range(column_count):
                if row[column_index] == "1":
                    heights[column_index] += 1
                else:
                    heights[column_index] = 0

            max_rectangle = max(max_rectangle, largest_rectangle_area(heights))

        return max_rectangle
