from .BinaryTreeMaximumPathSum import Solution
from .BinaryTreeMaximumPathSum import TreeNode

def test_binary_tree_maximum_path_sum():
    assert Solution().maxPathSum(TreeNode(-10,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))) == 42