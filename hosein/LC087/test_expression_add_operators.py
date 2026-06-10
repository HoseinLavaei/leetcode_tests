from .expression_add_operators import Solution

def test_expression_add_operators():
    assert sorted(Solution().addOperators("123",6)) == sorted(["1*2*3","1+2+3"])