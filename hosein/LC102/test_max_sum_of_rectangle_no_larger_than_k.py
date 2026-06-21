from .max_sum_of_rectangle_no_larger_than_k import Solution

def test_max_sum_of_rectangle_no_larger_than_k():
    assert Solution().maxSumSubmatrix(matrix = [[1,0,1],[0,-2,3]], k = 2) == 2