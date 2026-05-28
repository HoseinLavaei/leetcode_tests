from .SimplifyPath import Solution

def test_simplify_path():
    assert Solution().simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
