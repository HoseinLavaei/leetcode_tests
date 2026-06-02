from .WordSearch import Solution

def test_combinations():
    assert Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True