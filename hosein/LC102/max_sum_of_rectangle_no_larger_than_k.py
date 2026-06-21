from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        if m > n:
            matrix = [[matrix[i][j] for i in range(m)] for j in range(n)]
            m, n = n, m
        ans = float('-inf')
        for top in range(m):
            col_sum = [0] * n
            for bottom in range(top, m):
                for j in range(n):
                    col_sum[j] += matrix[bottom][j]
                prefix = [0]
                curr = 0
                for val in col_sum:
                    curr += val
                    target = curr - k
                    idx = bisect.bisect_left(prefix, target)
                    if idx < len(prefix):
                        candidate = curr - prefix[idx]
                        if candidate > ans:
                            ans = candidate
                            if ans == k:
                                return k
                    bisect.insort(prefix, curr)
        return ans