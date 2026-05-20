from .GenerateParentheses import Solution

def test_generate_parentheses():
    assert Solution().generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]