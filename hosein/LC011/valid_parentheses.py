class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        counter = 0

        while counter < len(s):
            current = s[counter]

            if current in "([{":
                stack.append(current)
            elif stack and current == get_close_parentheses(stack[-1]):
                stack.pop()
            else:
                return False

            counter += 1

        return stack == []

def get_close_parentheses(s: str) -> str | None:
    if s == "(":
        return ")"
    if s == "[":
        return "]"
    if s == "{":
        return "}"
    return None