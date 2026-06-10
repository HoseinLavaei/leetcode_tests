from .substring_with_concatenation_of_all_words import Solution

def test_substring_with_concatenation_of_all_words():
    assert Solution().findSubstring("barfoothefoobarman", ["foo","bar"]) == [0,9]