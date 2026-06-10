from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_count = len(board)
        column_count = len(board[0])

        def search_from_cell(row_index: int, column_index: int, word_index: int) -> bool:
            if word_index == len(word):
                return True

            if row_index < 0 or row_index == row_count:
                return False
            if column_index < 0 or column_index == column_count:
                return False
            if board[row_index][column_index] != word[word_index]:
                return False

            original_character = board[row_index][column_index]
            board[row_index][column_index] = "#"

            word_found = (
                search_from_cell(row_index + 1, column_index, word_index + 1)
                or search_from_cell(row_index - 1, column_index, word_index + 1)
                or search_from_cell(row_index, column_index + 1, word_index + 1)
                or search_from_cell(row_index, column_index - 1, word_index + 1)
            )

            board[row_index][column_index] = original_character
            return word_found

        for row_index in range(row_count):
            for column_index in range(column_count):
                if search_from_cell(row_index, column_index, 0):
                    return True

        return False
