from .next_permutation import Solution

def test_next_permutation():
    nums = [1,2,3]
    Solution().nextPermutation(nums)
    assert nums == [1,3,2]