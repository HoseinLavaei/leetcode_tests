from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        result = []
        max_heap = [(0, float('inf'))]

        for position, neg_height, end_position in events:

            while max_heap[0][1] <= position:
                heapq.heappop(max_heap)

            if neg_height != 0:
                heapq.heappush(max_heap, (neg_height, end_position))

            current_height = -max_heap[0][0]

            if not result or result[-1][1] != current_height:
                result.append([position, current_height])

        return result