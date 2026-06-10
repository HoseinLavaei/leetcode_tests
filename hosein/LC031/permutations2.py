from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        result: List[List[int]] = []
        used_values = set()

        for num_index in range(len(nums)):
            chosen = nums[num_index]

            if chosen in used_values:
                continue

            used_values.add(chosen)

            remaining = nums[:num_index] + nums[num_index + 1:]

            for permutation in self.permuteUnique(remaining):
                result.append([chosen] + permutation)

        return result