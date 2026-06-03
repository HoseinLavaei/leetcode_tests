from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        number_of_rows, number_of_cols = len(board), len(board[0])
        found_words = []

        trie_root = {}

        for word in words:
            current_trie_node = trie_root
            for character in word:
                current_trie_node = current_trie_node.setdefault(character, {})
            current_trie_node["end_word"] = word

        def depth_first_search(row_index, col_index, current_trie_node):
            if (
                row_index < 0 or row_index >= number_of_rows or
                col_index < 0 or col_index >= number_of_cols or
                board[row_index][col_index] not in current_trie_node
            ):
                return

            current_character = board[row_index][col_index]
            next_trie_node = current_trie_node[current_character]

            if "end_word" in next_trie_node:
                found_words.append(next_trie_node["end_word"])
                del next_trie_node["end_word"]

            board[row_index][col_index] = "#"

            depth_first_search(row_index + 1, col_index, next_trie_node)
            depth_first_search(row_index - 1, col_index, next_trie_node)
            depth_first_search(row_index, col_index + 1, next_trie_node)
            depth_first_search(row_index, col_index - 1, next_trie_node)

            board[row_index][col_index] = current_character

            if not next_trie_node:
                current_trie_node.pop(current_character)

        for row_index in range(number_of_rows):
            for col_index in range(number_of_cols):
                depth_first_search(row_index, col_index, trie_root)

        return found_words