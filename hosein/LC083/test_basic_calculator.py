from .basic_calculator import Solution

def test_basic_calculator():
    assert Solution().calculate("7 + (4 - 3 + (-1))") == 7