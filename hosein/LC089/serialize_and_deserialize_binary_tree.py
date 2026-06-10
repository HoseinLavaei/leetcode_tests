class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return ""
        left_serial = self.serialize(root.left)
        right_serial = self.serialize(root.right)
        return f"{root.val},{left_serial},{right_serial}"

    def deserialize(self, data:str) -> TreeNode:
        if not data:
            return None
        tokens = data.split(',')
        position = 0

        def build_tree() -> TreeNode:
            nonlocal position
            current_token = tokens[position]
            position += 1
            if current_token == "":
                return None
            node = TreeNode(int(current_token))
            node.left = build_tree()
            node.right = build_tree()
            return node

        return build_tree()