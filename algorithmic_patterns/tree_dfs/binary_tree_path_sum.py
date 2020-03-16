"""
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the
node values of that path equals ‘S’.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.left.data}<-{self.data}->{self.right.data}'


def binary_tree_path_sum(node: TreeNode, target_sum):
    if not node:
        return False

    if not node.left and not node.right and target_sum == node.data:
        return True

    return binary_tree_path_sum(node.left, target_sum - node.data) or \
           binary_tree_path_sum(node.right, target_sum - node.data)


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print(binary_tree_path_sum(root, 26))