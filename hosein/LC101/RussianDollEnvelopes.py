from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in envelopes]
        lis = []
        for height in heights:
            position = bisect_left(lis, height)
            if position == len(lis):
                lis.append(height)
            else:
                lis[position] = height
        return len(lis)
