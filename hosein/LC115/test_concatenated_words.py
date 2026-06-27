from .concatenated_words import Solution

def test_concatenated_words():
    assert sorted(Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])) == sorted(["catsdogcats","dogcatsdog","ratcatdogcat"])