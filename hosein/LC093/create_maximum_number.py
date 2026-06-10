class Solution:
    def maxNumber(self, first_array: list[int], second_array: list[int], total_length: int) -> list[int]:

        best_result = []
        first_len = len(first_array)
        second_len = len(second_array)

        for take_from_first in range(max(0, total_length - second_len), min(total_length, first_len) + 1):
            take_from_second = total_length - take_from_first
            if take_from_second < 0 or take_from_second > second_len:
                continue
            subsequence_first = max_subsequence(first_array, take_from_first)
            subsequence_second = max_subsequence(second_array, take_from_second)
            candidate = merge_sequences(subsequence_first, subsequence_second)
            if candidate > best_result:
                best_result = candidate

        return best_result

def max_subsequence(source_array: list[int], subsequence_length: int) -> list[int]:
    if subsequence_length == 0:
        return []
    stack = []
    elements_to_remove = len(source_array) - subsequence_length
    for current_digit in source_array:
        while elements_to_remove > 0 and stack and stack[-1] < current_digit:
            stack.pop()
            elements_to_remove -= 1
        stack.append(current_digit)
    return stack[:subsequence_length]

def merge_sequences(first_seq: list[int], second_seq: list[int]) -> list[int]:
    merged_result = []
    first_index = 0
    second_index = 0
    while first_index < len(first_seq) and second_index < len(second_seq):
        if first_seq[first_index:] > second_seq[second_index:]:
            merged_result.append(first_seq[first_index])
            first_index += 1
        else:
            merged_result.append(second_seq[second_index])
            second_index += 1
    merged_result.extend(first_seq[first_index:])
    merged_result.extend(second_seq[second_index:])
    return merged_result
