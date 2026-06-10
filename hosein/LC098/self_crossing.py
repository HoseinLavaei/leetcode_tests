class Solution:
    def isSelfCrossing(self, distances: list[int]) -> bool:
        for i in range(3, len(distances)):
            # Case 1: current line crosses the line three steps behind
            if distances[i] >= distances[i - 2] and distances[i - 1] <= distances[i - 3]:
                return True

            # Case 2: current line crosses the line four steps behind
            if i >= 4 and distances[i - 1] == distances[i - 3] and distances[i] + distances[i - 4] >= distances[i - 2]:
                return True

            # Case 3: current line crosses the line five steps behind
            if i >= 5 and distances[i - 4] <= distances[i - 2] <= distances[i] + distances[i - 4] and distances[i - 1] <= distances[i - 3] and distances[i - 1] + distances[i - 5] >= distances[i - 3]:
                return True

        return False
