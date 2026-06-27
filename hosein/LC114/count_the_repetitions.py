class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        len1, len2 = len(s1), len(s2)
        repeat = [0] * len2
        next_idx = [0] * len2
        for i in range(len2):
            j = i
            cnt = 0
            for ch in s1:
                if ch == s2[j]:
                    j += 1
                    if j == len2:
                        cnt += 1
                        j = 0
            repeat[i] = cnt
            next_idx[i] = j
        idx = 0
        total = 0
        seen = {}
        i = 0
        while i < n1:
            if idx in seen:
                prev_s1, prev_total = seen[idx]
                cycle_s1 = i - prev_s1
                cycle_total = total - prev_total
                if cycle_s1 > 0:
                    cycles = (n1 - i) // cycle_s1
                    total += cycles * cycle_total
                    i += cycles * cycle_s1
                    if i >= n1:
                        break
            seen[idx] = (i, total)
            total += repeat[idx]
            idx = next_idx[idx]
            i += 1
        return total // n2