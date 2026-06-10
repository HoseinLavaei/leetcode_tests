class Solution:
    def countDigitOne(self, number: int) -> int:
        total_ones = 0
        position_factor = 1

        while position_factor <= number:
            higher_part = number // (position_factor * 10)
            current_digit = (number // position_factor) % 10
            lower_part = number % position_factor

            if current_digit == 0:
                total_ones += higher_part * position_factor
            elif current_digit == 1:
                total_ones += higher_part * position_factor + lower_part + 1
            else:
                total_ones += (higher_part + 1) * position_factor

            position_factor *= 10

        return total_ones