from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def max_gain_from_node(node: Optional[TreeNode]) -> int:
            nonlocal max_path_sum

            if node is None:
                return 0

            left_gain = max(max_gain_from_node(node.left), 0)
            right_gain = max(max_gain_from_node(node.right), 0)

            path_through_node = node.val + left_gain + right_gain
            max_path_sum = max(max_path_sum, path_through_node)

            return node.val + max(left_gain, right_gain)

        max_gain_from_node(root)
        return max_path_sum
