from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return SudokuViewer(board).validate()


class SudokuViewer:
    sudoku: List[List[str]]
    def __init__(self, sudoku: List[List[str]]) -> None:
        if len(sudoku) != 9:
            raise ValueError
        for i in range(9):
            if len(sudoku[i]) != 9:
                raise ValueError
        self.sudoku = sudoku
    def get(self, row: int, col: int) -> int:
        return int(self.sudoku[row][col])
    def get_row(self, row: int) -> List[str]:
        return self.sudoku[row]
    def get_col(self, col: int) -> List[str]:
        return [self.sudoku[i][col] for i in range(9)]
    def validate_line(self, is_row:bool, index:int) -> bool:
        line = None
        if is_row:
            line = self.get_row(index)
        else:
            line = self.get_col(index)
        flags = [False] * 9
        unknown_counter = 0
        for i in range(9):
            if line[i] == ".":
                unknown_counter += 1
            else:
                flags[int(line[i]) - 1] = True
        false_counter = 0
        for i in range(9):
            if not flags[i]:
                false_counter += 1
        if unknown_counter == false_counter:
            return True
        return all(flags)
    def validate(self) -> bool:
        flags = [False] * 9
        for i in range(9):
            flags[i] = self.validate_line(True,i) and self.validate_line(False,i)
        return all(flags)