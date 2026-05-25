from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0

        used_columns = set()
        used_positive_diagonals = set()
        used_negative_diagonals = set()

        def backtrack(row: int) -> None:
            nonlocal result

            if row == n:
                result += 1
                return

            for col in range(n):
                if col in used_columns:
                    continue

                if row + col in used_positive_diagonals:
                    continue

                if row - col in used_negative_diagonals:
                    continue

                used_columns.add(col)
                used_positive_diagonals.add(row + col)
                used_negative_diagonals.add(row - col)

                backtrack(row + 1)

                used_columns.remove(col)
                used_positive_diagonals.remove(row + col)
                used_negative_diagonals.remove(row - col)

        backtrack(0)
        return result