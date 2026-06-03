from .WordSearch2 import Solution

def test_word_search_2():
    assert sorted(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])) == sorted(["eat","oath"])