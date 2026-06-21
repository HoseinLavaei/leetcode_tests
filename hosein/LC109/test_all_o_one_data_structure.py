from .all_o_one_data_structure import AllOne


def test_all_o_one_data_structure():
    obj = AllOne()

    obj.inc("a")
    assert obj.getMaxKey() == "a"
    assert obj.getMinKey() == "a"

    obj.inc("b")
    obj.inc("b")
    assert obj.getMaxKey() == "b"
    assert obj.getMinKey() == "a"

    obj.dec("a")
    assert obj.getMaxKey() == "b"
    assert obj.getMinKey() == "b"

    obj.dec("b")
    assert obj.getMaxKey() == "b"
    assert obj.getMinKey() == "b"

    obj.dec("b")
    assert obj.getMaxKey() == ""
    assert obj.getMinKey() == ""