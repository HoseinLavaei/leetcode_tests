import enum
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return SudokuViewer(board).validate()

class LineType(enum.Enum):
    row = 0
    col = 1
    square = 2

class SudokuViewer:
    sudoku: List[List[str]]
    def __init__(self, sudoku: List[List[str]]) -> None:
        if len(sudoku) != 9:
            raise ValueError
        for i in range(9):
            if len(sudoku[i]) != 9:
                raise ValueError
        self.sudoku = sudoku
    def get(self, row: int, col: int) -> str:
        return self.sudoku[row][col]
    def get_row(self, row: int) -> List[str]:
        return self.sudoku[row]
    def get_col(self, col: int) -> List[str]:
        return [self.sudoku[i][col] for i in range(9)]
    def get_square(self, index: int) -> List[str]:
        square = []
        columns = []
        rows = []
        match index % 3:
            case 0:
                columns = [0,1,2]
            case 1:
                columns = [3,4,5]
            case 2:
                columns = [6,7,8]
            case _:
                raise ValueError
        match index // 3:
            case 0:
                rows = [0,1,2]
            case 1:
                rows = [3,4,5]
            case 2:
                rows = [6,7,8]
            case _:
                raise ValueError
        for row in rows:
            for col in columns:
                square.append(self.get(row,col))
        return square
    def validate_line(self, line_type:LineType, index:int) -> bool:
        line = None
        match line_type:
            case LineType.row:
                line = self.get_row(index)
            case LineType.col:
                line = self.get_col(index)
            case LineType.square:
                line = self.get_square(index)
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
        for i in range(9):
            # x,y,z = self.validate_line(LineType.row,i) , self.validate_line(LineType.col,i),  self.validate_line(LineType.square,i)
            if not (self.validate_line(LineType.row,i) and self.validate_line(LineType.col,i) and self.validate_line(LineType.square,i)):
                return False
        return True