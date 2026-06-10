from .zigzag_conversion import Solution

def test_zigzag_conversion() -> None:
    the_string = "PAYPALISHIRING"
    assert Solution().convert(the_string,3) == "PAHNAPLSIIGYIR"