from .simplify_path import Solution

def test_simplify_path():
    assert Solution().simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
