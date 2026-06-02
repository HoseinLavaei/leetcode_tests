from .SortColors import Solution

def test_sort_colors():
    objects = [2,0,2,1,1,0]
    Solution().sortColors(objects)
    assert objects == [0,0,1,1,2,2]