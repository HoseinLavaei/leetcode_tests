from .RemoveDuplicatesFromSortedArray2 import Solution


def test_remove_duplicates_from_sorted_array_2():
    nums = [1, 1, 1, 2, 2, 3]
    k = Solution().removeDuplicates(nums)
    assert k == 5
    assert nums[:k] == [1, 1, 2, 2, 3]
