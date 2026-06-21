class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(p: int) -> int:
            count = 0
            first = p
            next_p = p + 1
            while first <= n:
                count += min(n + 1, next_p) - first
                first *= 10
                next_p *= 10
            return count

        curr = 1
        k -= 1
        while k > 0:
            cnt = count_prefix(curr)
            if cnt <= k:
                k -= cnt
                curr += 1
            else:
                k -= 1
                curr *= 10
        return curr