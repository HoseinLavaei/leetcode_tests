from .longest_substring_without_repeating_characters import Solution

def test_lswrc():
    s = "abcabcbb"
    t = Solution().lengthOfLongestSubstring(s)
    assert t == 3