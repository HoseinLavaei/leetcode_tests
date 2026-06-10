from .valid_number import Solution

def test_valid_number():
    # power to a float is false for this question.
    assert Solution().isNumber("+5E3.14e-2") == False
