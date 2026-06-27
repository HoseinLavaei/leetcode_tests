from .lfu_cache import LFUCache

def test_lfu_cache():
    cache = LFUCache(2)

    assert cache.put(1, 1) is None
    assert cache.put(2, 2) is None
    assert cache.get(1) == 1
    assert cache.put(3, 3) is None
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    assert cache.put(4, 4) is None
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4