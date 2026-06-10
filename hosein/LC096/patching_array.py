class Solution:
    def minPatches(self, numbers: list[int], target_number: int) -> int:
        max_reachable = 0
        patch_count = 0
        index = 0
        array_length = len(numbers)

        while max_reachable < target_number:
            if index < array_length and numbers[index] <= max_reachable + 1:
                max_reachable += numbers[index]
                index += 1
            else:
                max_reachable += max_reachable + 1
                patch_count += 1

        return patch_count