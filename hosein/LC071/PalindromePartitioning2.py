class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # is_pal[i][j] = True if s[i:j+1] is a palindrome
        is_pal = [[False] * n for _ in range(n)]

        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (
                    right - left <= 2 or is_pal[left + 1][right - 1]
                ):
                    is_pal[left][right] = True

        # dp[i] = minimum cuts needed for s[:i+1]
        dp = [0] * n

        for i in range(n):
            if is_pal[0][i]:
                dp[i] = 0
            else:
                dp[i] = float("inf")

                for j in range(i):
                    if is_pal[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]