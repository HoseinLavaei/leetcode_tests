from .WildcardMatching import Solution

def test_wildcard_matching():
    assert Solution().isMatch("adceb", "*a*b") == True
