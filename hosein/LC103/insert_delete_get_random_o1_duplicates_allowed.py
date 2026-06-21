import random

class RandomizedCollection:
    def __init__(self):
        self.vals = []
        self.idx_map = {}

    def insert(self, val: int) -> bool:
        not_present = val not in self.idx_map
        self.idx_map.setdefault(val, set()).add(len(self.vals))
        self.vals.append(val)
        return not_present

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        idx_to_remove = next(iter(self.idx_map[val]))
        last_idx = len(self.vals) - 1
        if idx_to_remove != last_idx:
            last_val = self.vals[last_idx]
            self.vals[idx_to_remove] = last_val
            self.idx_map[last_val].remove(last_idx)
            self.idx_map[last_val].add(idx_to_remove)
        self.vals.pop()
        self.idx_map[val].remove(idx_to_remove)
        if not self.idx_map[val]:
            del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)