from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, cnt_left = merge_sort(arr[:mid])
            right, cnt_right = merge_sort(arr[mid:])
            merged = []
            i = j = 0
            cnt = cnt_left + cnt_right

            for val in left:
                while j < len(right) and val > 2 * right[j]:
                    j += 1
                cnt += j

            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, cnt

        _, ans = merge_sort(nums)
        return ans