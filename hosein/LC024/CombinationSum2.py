from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start: int, current: List[int], total: int):
            if total == target:
                result.append(current.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])
                backtrack(i + 1, current, total + candidates[i])
                current.pop()

        backtrack(0, [], 0)
        return result