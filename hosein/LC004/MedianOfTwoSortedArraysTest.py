from .MedianOfTwoSortedArrays import Solution

def test_median_of_two_sorted_arrays():
    num1 = [1,2]
    num2 = [3,4]
    assert Solution().findMedianSortedArrays(num1, num2) == 2.5

    num1 = [1,3]
    num2 = [2]
    assert Solution().findMedianSortedArrays(num1, num2) == 2