from .russian_doll_envelopes import Solution

def test_russian_doll_envelopes():
    assert Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3