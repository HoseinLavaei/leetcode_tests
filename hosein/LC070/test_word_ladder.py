from .word_ladder import Solution

def test_word_ladder():
    assert Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]) == 5