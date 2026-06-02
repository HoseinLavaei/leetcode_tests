from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        needed = Counter(t)
        window = defaultdict(int)
        required = len(needed)
        formed = 0

        best_start = 0
        best_len = float("inf")
        left = 0

        for right, char in enumerate(s):
            window[char] += 1

            if char in needed and window[char] == needed[char]:
                formed += 1

            while formed == required:
                current_len = right - left + 1
                if current_len < best_len:
                    best_start = left
                    best_len = current_len

                left_char = s[left]
                window[left_char] -= 1
                if left_char in needed and window[left_char] < needed[left_char]:
                    formed -= 1

                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_start:best_start + best_len]
