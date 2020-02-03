"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a
subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_a_subtree(source_node: TreeNode, target_node: TreeNode):
    if not source_node:
        return True
    if not target_node:
        return False
    if is_equal(source_node, target_node):
        return True
    return is_a_subtree(source_node, target_node.left) or is_a_subtree(source_node, target_node.right)


def is_equal(source_node: TreeNode, target_node: TreeNode):
    if not source_node or not target_node:
        return False
    elif not source_node and not target_node:
        return True
    return source_node.val == target_node.val and \
           is_equal(source_node.left, target_node.left) and \
           is_equal(source_node.right, target_node.right)


if __name__ == '__main__':
    T = TreeNode(26)
    T.right = TreeNode(3)
    T.right.right = TreeNode(3)
    T.left = TreeNode(10)
    T.left.left = TreeNode(4)
    T.left.left.right = TreeNode(30)
    T.left.right = TreeNode(6)

    S = TreeNode(10)
    S.right = TreeNode(6)
    S.left = TreeNode(4)
    S.left.right = TreeNode(30)
    print(is_a_subtree(T, S))

