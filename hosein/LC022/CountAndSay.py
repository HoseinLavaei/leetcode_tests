class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return say(self.countAndSay(n - 1))


def say(string: str) -> str:
    output = ""
    current_digit = string[0]
    current_times = 1

    for i in range(1, len(string)):
        if string[i] == current_digit:
            current_times += 1
        else:
            output += str(current_times) + current_digit
            current_digit = string[i]
            current_times = 1

    output += str(current_times) + current_digit
    return output