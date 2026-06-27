from collections import OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.freq_map = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        value, freq = self.key_map[key]
        self._update(key, value, freq)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_map:
            _, freq = self.key_map[key]
            self.key_map[key][0] = value
            self._update(key, value, freq)
        else:
            if len(self.key_map) >= self.capacity:
                self._evict()
            self.key_map[key] = [value, 1]
            if 1 not in self.freq_map:
                self.freq_map[1] = OrderedDict()
            self.freq_map[1][key] = None
            self.min_freq = 1

    def _update(self, key: int, value: int, old_freq: int) -> None:
        self.freq_map[old_freq].pop(key)
        if not self.freq_map[old_freq]:
            del self.freq_map[old_freq]
            if self.min_freq == old_freq:
                while self.min_freq not in self.freq_map or not self.freq_map[self.min_freq]:
                    self.min_freq += 1
        new_freq = old_freq + 1
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = OrderedDict()
        self.freq_map[new_freq][key] = None
        self.key_map[key] = [value, new_freq]

    def _evict(self) -> None:
        lru_key, _ = self.freq_map[self.min_freq].popitem(last=False)
        del self.key_map[lru_key]
        if not self.freq_map[self.min_freq]:
            del self.freq_map[self.min_freq]