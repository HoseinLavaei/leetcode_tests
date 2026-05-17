from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = [""]
        for digit in digits:
            letters = get_letters(digit)
            result = [prefix + letter for prefix in result for letter in letters]
        return result


def get_letters(digit: str) -> List[str]:
    match digit:
        case "2":
            return ["a", "b", "c"]
        case "3":
            return ["d", "e", "f"]
        case "4":
            return ["g", "h", "i"]
        case "5":
            return ["j", "k", "l"]
        case "6":
            return ["m", "n", "o"]
        case "7":
            return ["p", "q", "r", "s"]
        case "8":
            return ["t", "u", "v"]
        case "9":
            return ["w", "x", "y", "z"]
        case _:
            raise ValueError
