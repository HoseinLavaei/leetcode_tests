class Solution:
    def countRangeSum(self, numbers: list[int], lower_bound: int, upper_bound: int) -> int:
        prefix_sums = [0]
        for value in numbers:
            prefix_sums.append(prefix_sums[-1] + value)

        def merge_sort_and_count(start_index: int, end_index: int) -> int:
            if end_index - start_index <= 1:
                return 0
            middle_index = (start_index + end_index) // 2
            left_count = merge_sort_and_count(start_index, middle_index)
            right_count = merge_sort_and_count(middle_index, end_index)

            cross_count = 0
            left_pointer = start_index
            right_lower_pointer = middle_index
            right_upper_pointer = middle_index

            for left_pointer in range(start_index, middle_index):
                while right_lower_pointer < end_index and prefix_sums[right_lower_pointer] - prefix_sums[
                    left_pointer] < lower_bound:
                    right_lower_pointer += 1
                while right_upper_pointer < end_index and prefix_sums[right_upper_pointer] - prefix_sums[
                    left_pointer] <= upper_bound:
                    right_upper_pointer += 1
                cross_count += right_upper_pointer - right_lower_pointer

            merged_array = []
            left_part_start = start_index
            right_part_start = middle_index
            while left_part_start < middle_index and right_part_start < end_index:
                if prefix_sums[left_part_start] <= prefix_sums[right_part_start]:
                    merged_array.append(prefix_sums[left_part_start])
                    left_part_start += 1
                else:
                    merged_array.append(prefix_sums[right_part_start])
                    right_part_start += 1
            merged_array.extend(prefix_sums[left_part_start:middle_index])
            merged_array.extend(prefix_sums[right_part_start:end_index])
            prefix_sums[start_index:end_index] = merged_array

            return left_count + right_count + cross_count

        total_count = merge_sort_and_count(0, len(prefix_sums))
        return total_count