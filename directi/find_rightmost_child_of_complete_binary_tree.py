"""
Rightmost child of a complete binary tree
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rightmost_child_of_complete_binary_tree(root: TreeNode, height_of_the_tree: int):
    if root is None or height_of_the_tree < 1:
        return None
    if height_of_the_tree == 1:
        return root
    height_copy = height_of_the_tree
    while height_copy & (height_copy - 1):
        height_copy &= (height_copy - 1)

    height_copy >>= 1
    return