from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row_length = len(matrix)
        result = [[0 for _ in range(row_length)] for _ in range(row_length)]

        for row in range(row_length):
            for col in range(row_length):
                result[col][row_length - 1 - row] = matrix[row][col]

        matrix[:] = result