from .InsertIntervals import Solution


def test_insert_intervals():
    assert Solution().insert([[1,3],[6,9]],[2,5]) == [[1,5],[6,9]]
