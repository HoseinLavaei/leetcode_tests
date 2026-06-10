class Solution:
    def reverse(self, x: int) -> int:
        reversed_string = str(x)[::-1]
        negative = False
        if reversed_string[len(reversed_string) - 1] == '-':
            negative = True
            reversed_string = reversed_string.removesuffix("-")
        reversed_integer = int(reversed_string)
        if reversed_integer >= 2 ** 32:
            return 0
        if negative:
            reversed_integer = -reversed_integer
        return reversed_integer
