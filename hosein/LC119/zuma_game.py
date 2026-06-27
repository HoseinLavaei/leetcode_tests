from functools import lru_cache
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        self.hand_counts = Counter(hand)
        self.color_map = {'R': 0, 'Y': 1, 'B': 2, 'G': 3, 'W': 4}
        INF = 10**9

        @lru_cache(None)
        def reduce_board(b: str) -> str:
            changed = True
            while changed:
                changed = False
                i = 0
                new_b = []
                while i < len(b):
                    j = i
                    while j < len(b) and b[j] == b[i]:
                        j += 1
                    if j - i >= 3:
                        changed = True
                        i = j
                    else:
                        new_b.append(b[i:j])
                        i = j
                b = ''.join(new_b)
            return b

        @lru_cache(None)
        def dfs(board_str: str, hand_tuple: tuple) -> int:
            board_str = reduce_board(board_str)
            if not board_str:
                return 0

            if sum(hand_tuple) == 0:
                return INF

            min_balls = INF
            # Try all possible insertions
            for i in range(len(board_str) + 1):
                for color_idx, cnt in enumerate(hand_tuple):
                    if cnt == 0:
                        continue
                    color = list(self.color_map.keys())[list(self.color_map.values()).index(color_idx)]  # reverse mapping
                    # Optional optimization: only insert if it matches neighbor or board is empty (but board not empty here)
                    # Actually we can restrict to inserting where it matches at least one neighbor to reduce search.
                    # But to be safe, try all.
                    new_board = board_str[:i] + color + board_str[i:]
                    new_board = reduce_board(new_board)
                    new_hand = list(hand_tuple)
                    new_hand[color_idx] -= 1
                    result = dfs(new_board, tuple(new_hand))
                    if result != INF:
                        min_balls = min(min_balls, 1 + result)

            return min_balls

        # Convert hand to tuple of counts
        hand_tuple = tuple(self.hand_counts.get(color, 0) for color in ['R', 'Y', 'B', 'G', 'W'])
        ans = dfs(board, hand_tuple)
        return ans if ans != INF else -1