from .data_stream_as_disjoint_intervals import SummaryRanges

def test_data_stream_as_disjoint_intervals():
    obj = SummaryRanges()
    obj.addNum(1)
    assert obj.getIntervals() == [[1, 1]]

    obj.addNum(3)
    assert obj.getIntervals() == [[1, 1], [3, 3]]

    obj.addNum(7)
    assert obj.getIntervals() == [[1, 1], [3, 3], [7, 7]]

    obj.addNum(2)
    assert obj.getIntervals() == [[1, 3], [7, 7]]

    obj.addNum(6)
    assert obj.getIntervals() == [[1, 3], [6, 7]]