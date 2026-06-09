class Solution:
    def countSmaller(self, numbers: list[int]) -> list[int]:
        if not numbers:
            return []

        sorted_unique = sorted(set(numbers))
        value_to_rank = {value: index + 1 for index, value in enumerate(sorted_unique)}
        total_ranks = len(sorted_unique)

        bit = [0] * (total_ranks + 2)

        def bit_update(index: int) -> None:
            while index <= total_ranks:
                bit[index] += 1
                index += index & -index

        def bit_query(index: int) -> int:
            prefix_sum = 0
            while index > 0:
                prefix_sum += bit[index]
                index -= index & -index
            return prefix_sum

        result = [0] * len(numbers)
        for position in range(len(numbers) - 1, -1, -1):
            current_rank = value_to_rank[numbers[position]]
            smaller_count = bit_query(current_rank - 1)
            result[position] = smaller_count
            bit_update(current_rank)

        return result