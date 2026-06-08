class Solution:
    def calculate(self, expression_string: str) -> int:
        current_result = 0
        current_sign = 1
        current_number = 0
        result_stack = []

        for character in expression_string:
            if character.isdigit():
                current_number = current_number * 10 + int(character)

            elif character == '+':
                current_result += current_sign * current_number
                current_number = 0
                current_sign = 1

            elif character == '-':
                current_result += current_sign * current_number
                current_number = 0
                current_sign = -1

            elif character == '(':
                result_stack.append((current_result, current_sign))
                current_result = 0
                current_sign = 1
                current_number = 0

            elif character == ')':
                current_result += current_sign * current_number
                previous_result, previous_sign = result_stack.pop()
                current_result = previous_result + previous_sign * current_result
                current_number = 0
                current_sign = 1

        current_result += current_sign * current_number
        return current_result