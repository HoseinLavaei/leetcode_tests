from typing import List
from hosein.LC003.ValidSudoku import Solution as _Solution, SudokuViewer


## Attention:
## This Solver can't solve boards that need guessing. If you give it such a board, it will run until it gives you recursion error.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not _Solution().isValidSudoku(board):
            return
        unknowns: list[tuple[int,list[int]]] = [] # add tuples : (index,[possible]) where index is 9 * row + col
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    unknowns.append((row * 9 + col, get_possible(board, row * 9 + col)))
        for element in unknowns:
            if len(element[1]) == 1:
                index = element[0]
                row_index = index // 9
                col_index = index % 9
                board[row_index][col_index] = str(element[1][0])
        is_solved = True
        for row in board:
            for element in row:
                if element == ".":
                    is_solved = False
                    break
        if is_solved:
            return
        Solution().solveSudoku(board)
def get_possible(board, index:int) -> List[int]:
    possibles = []
    row_index = index // 9
    col_index = index % 9
    square_index = (row_index // 3) * 3 + (col_index // 3)
    sudoku_viewer = SudokuViewer(board)
    row = sudoku_viewer.get_row(row_index)
    col = sudoku_viewer.get_col(col_index)
    square = sudoku_viewer.get_square(square_index)
    for i in range(1,10):
        if not str(i) in row and not str(i) in col and not str(i) in square:
            possibles.append(i)
    return possibles