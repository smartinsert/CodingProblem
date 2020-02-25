"""
Given a binary tree, return the inorder traversal of its nodes’ values.
Inorder: left -> root -> right
"""

from typing import List


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_traversal(node: TreeNode, result) -> List[int]:
    # Base case
    if not node:
        return result

    in_order_traversal(node.left, result)
    result.append(node.data)
    in_order_traversal(node.right, result)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3

    traversal = []
    in_order_traversal(node1, traversal)

    print(traversal)


