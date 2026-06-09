from .PalindromePairs import Solution

def test_palindrome_pairs():
    assert sorted(Solution().palindromePairs(["abcd","dcba","lls","s","sssll"])) == sorted([[0,1],[1,0],[3,2],[2,4]])