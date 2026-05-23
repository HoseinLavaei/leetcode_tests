class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])

                product = digit1 * digit2

                position = i + j + 1
                total = result[position] + product

                result[position] = total % 10
                result[position - 1] += total // 10

        return "".join(str(digit) for digit in result).lstrip("0")