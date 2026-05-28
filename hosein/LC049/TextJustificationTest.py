from .TextJustification import Solution

def test_text_justification():
    assert Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == ["This    is    an", "example  of text", "justification.  "]
