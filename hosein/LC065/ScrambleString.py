from functools import cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        @cache
        def can_scramble(first: str, second: str) -> bool:
            if first == second:
                return True

            if sorted(first) != sorted(second):
                return False

            length = len(first)
            for split_index in range(1, length):
                no_swap = (
                    can_scramble(first[:split_index], second[:split_index])
                    and can_scramble(first[split_index:], second[split_index:])
                )
                if no_swap:
                    return True

                with_swap = (
                    can_scramble(first[:split_index], second[length - split_index:])
                    and can_scramble(first[split_index:], second[:length - split_index])
                )
                if with_swap:
                    return True

            return False

        return can_scramble(s1, s2)
