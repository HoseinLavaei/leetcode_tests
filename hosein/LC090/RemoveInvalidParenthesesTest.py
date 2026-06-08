from .RemoveInvalidParentheses import Solution

def test_remove_invalid_parentheses():
    assert sorted(Solution().removeInvalidParentheses("()())()")) == sorted(["(())()","()()()"])