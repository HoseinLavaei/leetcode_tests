from .word_break2 import Solution

def test_word_break_2():
    assert sorted(Solution().wordBreak("pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"])) == sorted(["pine apple pen apple","pineapple pen apple","pine applepen apple"])