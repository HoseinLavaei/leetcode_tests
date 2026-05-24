from .Pow import Solution


def test_pow():
    # I couldn't test it simple cause of floating point error, and LeetCode didn't let me return Decimal, so I checked if the difference is little, pass it
    assert abs(Solution().myPow(2.1, 3) - 9.26100) < 0.00001