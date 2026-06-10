from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        result = []

        for size in range(n, 0, -1):
            group_size = factorial(size - 1)
            index = (k-1) // group_size

            result.append(numbers.pop(index))
            k %= group_size

        return "".join(result)