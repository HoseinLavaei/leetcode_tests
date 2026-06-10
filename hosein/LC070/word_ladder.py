from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        available_words = set(wordList)

        if endWord not in available_words:
            return 0

        words_to_visit = deque([(beginWord, 1)])
        available_words.discard(beginWord)

        while words_to_visit:
            current_word, transformation_length = words_to_visit.popleft()

            if current_word == endWord:
                return transformation_length

            for character_index in range(len(current_word)):
                for replacement_character in "abcdefghijklmnopqrstuvwxyz":
                    if replacement_character == current_word[character_index]:
                        continue

                    next_word = (
                        current_word[:character_index]
                        + replacement_character
                        + current_word[character_index + 1:]
                    )

                    if next_word in available_words:
                        available_words.remove(next_word)
                        words_to_visit.append((next_word, transformation_length + 1))

        return 0
