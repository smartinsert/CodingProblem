"""
WAP to ascertain whether a binary tree is a mirror tree
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_a_mirror(node: TreeNode) -> bool:
    if not node:
        return True
    return is_symmetric(left=node.left, right=node.right)


def is_symmetric(left: TreeNode, right: TreeNode):
    if not left or not right:
        return left == right
    if left.data != right.data:
        return False
    return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(2)
    n6 = TreeNode(3)
    n7 = TreeNode(4)
    n1.left, n1.right = n2, n5
    n2.left, n2.right = n3, n4
    n5.left, n5.right = n7, n6
    print(is_a_mirror(n1))