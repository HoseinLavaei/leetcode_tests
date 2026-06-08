from collections import deque
from ..LC011.ValidParentheses import Solution as ValidParentheses

class Solution:
    def removeInvalidParentheses(self, expression_string: str) -> list[str]:
        if not expression_string:
            return [""]

        valid_expressions = []
        visited_expressions = set()
        level_queue = deque()
        level_queue.append(expression_string)
        found_valid = False

        while level_queue:
            current_size = len(level_queue)
            for _ in range(current_size):
                current_expression = level_queue.popleft()

                if ValidParentheses().isValid(current_expression):
                    valid_expressions.append(current_expression)
                    found_valid = True

                if found_valid:
                    continue

                for index in range(len(current_expression)):
                    character = current_expression[index]
                    if character not in ('(', ')'):
                        continue

                    next_expression = current_expression[:index] + current_expression[index + 1:]
                    if next_expression not in visited_expressions:
                        visited_expressions.add(next_expression)
                        level_queue.append(next_expression)

            if found_valid:
                break

        return valid_expressions if valid_expressions else [""]
