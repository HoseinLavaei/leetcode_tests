from .remove_invalid_parentheses import Solution

def test_remove_invalid_parentheses():
    assert sorted(Solution().removeInvalidParentheses("()())()")) == sorted(["(())()","()()()"])