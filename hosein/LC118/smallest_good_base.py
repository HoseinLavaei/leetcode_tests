class Solution:
    def smallestGoodBase(self, n: str) -> str:
        N = int(n)
        max_k = N.bit_length()
        for k in range(max_k, 1, -1):
            low, high = 2, int(N ** (1 / (k - 1))) + 1
            while low <= high:
                mid = (low + high) // 2
                total = sum(mid ** i for i in range(k))
                if total == N:
                    return str(mid)
                elif total < N:
                    low = mid + 1
                else:
                    high = mid - 1
        return str(N - 1)