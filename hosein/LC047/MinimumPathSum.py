from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue

                from_top = grid[row - 1][col] if row > 0 else float("inf")
                from_left = grid[row][col - 1] if col > 0 else float("inf")
                grid[row][col] += min(from_top, from_left)

        return grid[-1][-1]
