from .DungeonGame import Solution

def test_dungeon_game():
    assert Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]) == 7