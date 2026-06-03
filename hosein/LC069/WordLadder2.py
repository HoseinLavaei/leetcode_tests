from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if beginWord == endWord:
            return [[beginWord]]

        available_words = set(wordList)
        if endWord not in available_words:
            return []

        parent_words: DefaultDict[str, List[str]] = defaultdict(list)
        current_level = [beginWord]
        available_words.discard(beginWord)
        found_end_word = False

        while current_level and not found_end_word:
            next_level = []
            next_level_seen = set()

            for current_word in current_level:
                for character_index in range(len(current_word)):
                    for replacement_character in "abcdefghijklmnopqrstuvwxyz":
                        if replacement_character == current_word[character_index]:
                            continue

                        next_word = (
                            current_word[:character_index]
                            + replacement_character
                            + current_word[character_index + 1:]
                        )

                        if next_word not in available_words:
                            continue

                        parent_words[next_word].append(current_word)

                        if next_word not in next_level_seen:
                            next_level_seen.add(next_word)
                            next_level.append(next_word)

                        if next_word == endWord:
                            found_end_word = True

            available_words -= next_level_seen
            current_level = next_level

        if not found_end_word:
            return []

        shortest_paths: List[List[str]] = []
        current_path = [endWord]

        def build_paths_backwards(current_word: str) -> None:
            if current_word == beginWord:
                shortest_paths.append(current_path[::-1])
                return

            for parent_word in parent_words[current_word]:
                current_path.append(parent_word)
                build_paths_backwards(parent_word)
                current_path.pop()

        build_paths_backwards(endWord)
        return shortest_paths
