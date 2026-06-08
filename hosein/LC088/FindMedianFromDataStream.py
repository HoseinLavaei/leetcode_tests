import heapq


class MedianFinder:
    def __init__(self):
        self.lower_max_heap = []
        self.upper_min_heap = []

    def addNum(self, number: int) -> None:
        if not self.lower_max_heap or number <= -self.lower_max_heap[0]:
            heapq.heappush(self.lower_max_heap, -number)
        else:
            heapq.heappush(self.upper_min_heap, number)

        if len(self.lower_max_heap) > len(self.upper_min_heap) + 1:
            moved = -heapq.heappop(self.lower_max_heap)
            heapq.heappush(self.upper_min_heap, moved)
        elif len(self.upper_min_heap) > len(self.lower_max_heap):
            moved = heapq.heappop(self.upper_min_heap)
            heapq.heappush(self.lower_max_heap, -moved)

    def findMedian(self) -> float:
        if len(self.lower_max_heap) > len(self.upper_min_heap):
            return float(-self.lower_max_heap[0])
        else:
            return (-self.lower_max_heap[0] + self.upper_min_heap[0]) / 2.0