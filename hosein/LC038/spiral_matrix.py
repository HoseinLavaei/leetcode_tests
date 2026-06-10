from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1
        result = []

        while left <= right and up <= down:
            for col in range(left, right + 1):
                result.append(matrix[up][col])
            up += 1

            for row in range(up, down + 1):
                result.append(matrix[row][right])
            right -= 1

            if up <= down:
                for col in range(right, left - 1, -1):
                    result.append(matrix[down][col])
                down -= 1

            if left <= right:
                for row in range(down, up - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
