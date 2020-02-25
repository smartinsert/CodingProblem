"""
Complete the function to print spiral order traversal of a tree. For below tree, function
should print 1, 2, 3, 4, 5, 6, 7.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return '{}'.format(self.data)


def height(node: TreeNode):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


def level_order_traversal(node: TreeNode, level: int):
    if not node:
        return
    if level == 1:
        print(node)
    else:
        level_order_traversal(node.left, level - 1)
        level_order_traversal(node.right, level - 1)


def spiral_order_traversal(node: TreeNode, level: int, left_to_right: bool):
    if not node:
        return
    if level == 1:
        print(node)
    if left_to_right:
        spiral_order_traversal(node.left, level - 1, left_to_right)
        spiral_order_traversal(node.right, level - 1, left_to_right)
    else:
        spiral_order_traversal(node.right, level - 1, left_to_right)
        spiral_order_traversal(node.left, level - 1, left_to_right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)

    left_to_right = False

    for i in range(1, height(root) + 1):
        spiral_order_traversal(node=root, level=i, left_to_right=left_to_right)
        left_to_right = not left_to_right
