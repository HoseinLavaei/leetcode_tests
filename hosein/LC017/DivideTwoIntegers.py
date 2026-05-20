class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        for shift in range(31, -1, -1):
            if dividend >= divisor << shift:
                dividend -= divisor << shift
                result += 1 << shift

        if negative:
            result = -result

        return max(INT_MIN, min(INT_MAX, result))