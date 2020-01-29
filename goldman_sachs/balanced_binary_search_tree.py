class TreeNode:
    def __init(self, data):
        self.data = data
        self.left = None
        self.right = None


# Check if a tree is balanced
"""
A binary tree is said to be balanced if the difference in the height of the left and the right subtree is at most 1.
"""


def height_of(root: TreeNode) -> int:
    """
    :param root: root node of the tree
    :return: height of the tree
    """
    if not root:
        return 0
    return max(root.left, root.right) + 1


def is_balanced(root: TreeNode) -> bool:
    """
    :param root:  root node of the tree
    :return: whether the tree is balanced or not
    """
    if not root:
        return True
    left_height = height_of(root.left)
    right_height = height_of(root.right)
    if abs(right_height - left_height) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


# Check if a tree is a BST
"""
A binary tree is a binary search tree if all the nodes to the left of the root is less than the root which is in turn
less than the nodes to the right
"""


def is_bst(root: TreeNode, left_bound=-float('inf'), right_bound=float('inf')):
    if not root:
        return True
    return left_bound <= root.data <= right_bound and \
        is_bst(root.left, left_bound, root.data) and \
        is_bst(root.right, root.data, right_bound)



