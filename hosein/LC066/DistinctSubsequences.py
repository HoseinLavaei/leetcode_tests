class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        ways = [0] * (len(t) + 1)
        ways[0] = 1

        for source_character in s:
            for target_index in range(len(t) - 1, -1, -1):
                if source_character == t[target_index]:
                    ways[target_index + 1] += ways[target_index]

        return ways[len(t)]
