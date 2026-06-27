from .sliding_window_median import Solution

def test_sliding_window_median():
    assert Solution().medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3) == [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]