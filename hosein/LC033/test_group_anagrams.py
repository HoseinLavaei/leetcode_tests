from .group_anagrams import Solution

def test_group_anagrams():
    result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])