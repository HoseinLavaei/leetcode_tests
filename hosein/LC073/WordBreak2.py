from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in words:
                    for suffix in dfs(end):
                        if suffix:
                            result.append(word + " " + suffix)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return dfs(0)