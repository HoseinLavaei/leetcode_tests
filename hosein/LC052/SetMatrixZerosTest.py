from .SetMatrixZeros import Solution

def test_set_matrix_zeros():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1,0,1],[0,0,0],[1,0,1]]