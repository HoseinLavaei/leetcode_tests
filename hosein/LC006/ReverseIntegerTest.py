from .ReverseInteger import Solution

def test_reverse_integer():
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321