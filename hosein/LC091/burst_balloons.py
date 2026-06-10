class Solution:
    def maxCoins(self, balloon_values: list[int]) -> int:
        padded_values = [1] + balloon_values + [1]
        number_of_balloons = len(padded_values)

        dp_table = [[0] * number_of_balloons for _ in range(number_of_balloons)]

        for segment_length in range(2, number_of_balloons):
            for left_boundary in range(0, number_of_balloons - segment_length):
                right_boundary = left_boundary + segment_length
                for last_burst_index in range(left_boundary + 1, right_boundary):
                    coins_from_left = dp_table[left_boundary][last_burst_index]
                    coins_from_right = dp_table[last_burst_index][right_boundary]
                    coins_from_burst = padded_values[left_boundary] * padded_values[last_burst_index] * padded_values[right_boundary]
                    total_coins = coins_from_left + coins_from_right + coins_from_burst
                    dp_table[left_boundary][right_boundary] = max(dp_table[left_boundary][right_boundary], total_coins)

        return dp_table[0][number_of_balloons - 1]