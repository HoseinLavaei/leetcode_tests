from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                else:
                    if row > 0:
                        dp[row][col] += dp[row - 1][col]
                    if col > 0:
                        dp[row][col] += dp[row][col - 1]

        return dp[m - 1][n - 1]