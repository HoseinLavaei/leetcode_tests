from .insert_delete_get_random_o1_duplicates_allowed import RandomizedCollection


def test_insert_delete_get_random_o1_duplicates_allowed():
    obj = RandomizedCollection()

    assert obj.insert(1) == True
    assert obj.insert(1) == False
    assert obj.insert(2) == True

    r1 = obj.getRandom()
    assert r1 in (1, 2)

    assert obj.remove(1) == True

    r2 = obj.getRandom()
    assert r2 in (1, 2)

    assert obj.remove(1) == True

    r3 = obj.getRandom()
    assert r3 == 2

    assert obj.remove(2) == True

    assert obj.remove(3) == False