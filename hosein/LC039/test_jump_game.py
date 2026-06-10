from .jump_game import Solution


def test_jump_game():
    assert Solution().canJump([2,3,1,1,4]) == True
