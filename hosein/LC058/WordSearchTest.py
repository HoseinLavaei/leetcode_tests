from .WordSearch import Solution

def test_word_search():
    assert Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True