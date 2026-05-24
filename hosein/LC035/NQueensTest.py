from .NQueens import Solution


def test_n_queens():
    assert sorted(Solution().solveNQueens(4)) == sorted([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])