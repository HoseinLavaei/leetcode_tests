from .zuma_game import Solution

def test_zuma_game():
    assert Solution().findMinStep(board = "WRRBBW", hand = "RB") == -1