from collections import deque


class Solution:
    def maxSlidingWindow(self, numbers: list[int], window_size: int) -> list[int]:
        if not numbers:
            return []

        result_maximums = []
        monotonic_deque = deque()

        for current_index in range(len(numbers)):
            while monotonic_deque and numbers[monotonic_deque[-1]] <= numbers[current_index]:
                monotonic_deque.pop()

            monotonic_deque.append(current_index)

            if monotonic_deque[0] <= current_index - window_size:
                monotonic_deque.popleft()

            if current_index >= window_size - 1:
                result_maximums.append(numbers[monotonic_deque[0]])

        return result_maximums