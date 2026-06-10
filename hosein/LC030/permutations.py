from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        result: List[List[int]] = []

        for num_index in range(len(nums)):
            chosen = nums[num_index]
            remaining = nums[:num_index] + nums[num_index + 1:]

            rest = self.permute(remaining)

            for permutation in rest:
                result.append([chosen] + permutation)

        return result