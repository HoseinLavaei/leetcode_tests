from .word_ladder2 import Solution

def test_word_ladder_2():
    assert Solution().findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]) == [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]