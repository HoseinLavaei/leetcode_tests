import bisect


class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        position = bisect.bisect_left(self.intervals, [value, value])
        if position > 0 and self.intervals[position - 1][1] >= value - 1:
            position -= 1

        start_index = position
        end_index = position
        new_start = value
        new_end = value

        while end_index < len(self.intervals) and self.intervals[end_index][0] <= value + 1:
            new_start = min(new_start, self.intervals[end_index][0])
            new_end = max(new_end, self.intervals[end_index][1])
            end_index += 1

        self.intervals[start_index:end_index] = [[new_start, new_end]]

    def getIntervals(self) -> list[list[int]]:
        return self.intervals