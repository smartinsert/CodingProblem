"""
A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_symmetric(root):
    if not root:
        return True
    return is_symmetric_util(root.left, root.right)


def is_symmetric_util(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.data != right.data:
        return False
    return is_symmetric_util(left.left, right.right) and is_symmetric_util(left.right, right.left)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n5 = TreeNode(4)
    n6 = TreeNode(4)
    n7 = TreeNode(3)

    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7

    print(is_symmetric(n1))