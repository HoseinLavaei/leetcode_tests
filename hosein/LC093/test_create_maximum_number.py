from .create_maximum_number import Solution

def test_create_maximum_number():
    assert Solution().maxNumber([3,4,6,5], [9,1,2,5,8,3], 5) == [9,8,6,5,3]