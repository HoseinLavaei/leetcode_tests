from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        word_set = set()
        result = []

        for word in words:
            if word and self._can_form(word, word_set):
                result.append(word)
            word_set.add(word)

        return result

    def _can_form(self, word: str, word_set: set) -> bool:
        if not word_set:
            return False

        n = len(word)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and word[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]