from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result_expressions = []

        def backtrack(index, current_expression, current_value, last_operand):
            if index == len(num):
                if current_value == target:
                    result_expressions.append(current_expression)
                return

            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break

                substring = num[index:i + 1]
                operand = int(substring)

                if index == 0:
                    backtrack(i + 1, substring, operand, operand)
                else:
                    backtrack(i + 1, current_expression + "+" + substring, current_value + operand, operand)
                    backtrack(i + 1, current_expression + "-" + substring, current_value - operand, -operand)
                    new_value = (current_value - last_operand) + (last_operand * operand)
                    backtrack(i + 1, current_expression + "*" + substring, new_value, last_operand * operand)

        backtrack(0, "", 0, 0)
        return result_expressions
