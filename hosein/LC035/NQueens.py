from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result: List[List[str]] = []

        board = [["." for _ in range(n)] for _ in range(n)]

        used_columns = set()
        used_positive_diagonals = set()
        used_negative_diagonals = set()

        def backtrack(row: int) -> None:
            if row == n:
                result.append(["".join(board_row) for board_row in board])
                return

            for col in range(n):
                if col in used_columns:
                    continue

                if row + col in used_positive_diagonals:
                    continue

                if row - col in used_negative_diagonals:
                    continue

                board[row][col] = "Q"
                used_columns.add(col)
                used_positive_diagonals.add(row + col)
                used_negative_diagonals.add(row - col)

                backtrack(row + 1)

                board[row][col] = "."
                used_columns.remove(col)
                used_positive_diagonals.remove(row + col)
                used_negative_diagonals.remove(row - col)

        backtrack(0)
        return result