from .LongestSubstringWithoutRepeatingCharacters import Solution

def test_lswrc():
    s = "abcabcbb"
    t = Solution().lengthOfLongestSubstring(s)
    assert t == 3