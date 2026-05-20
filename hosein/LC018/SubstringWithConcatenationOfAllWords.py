from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count
        expected = Counter(words)
        result = []

        for start in range(len(s) - total_length + 1):
            seen = {}

            for i in range(word_count):
                word_start = start + i * word_length
                word = s[word_start:word_start + word_length]

                if word not in expected:
                    break

                seen[word] = seen.get(word, 0) + 1

                if seen[word] > expected[word]:
                    break
            else:
                result.append(start)

        return result