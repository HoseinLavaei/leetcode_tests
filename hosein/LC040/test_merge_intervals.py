from .merge_intervals import Solution


def test_merge_intervals():
    assert Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
