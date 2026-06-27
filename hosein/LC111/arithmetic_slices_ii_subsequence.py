from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = dp[j].get(d, 0)
                ans += cnt
                dp[i][d] = dp[i].get(d, 0) + cnt + 1
        return ans