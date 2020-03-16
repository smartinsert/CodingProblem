"""
Given a binary tree, return an array containing all the boundary nodes of the tree in an anti-clockwise direction.
"""

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_a_leaf(node: TreeNode):
    if not node.left and not node.right:
        return True
    return False


def find_tree_boundary(node: TreeNode):
    if not node:
        return []

    queue, left_children, right_children = list(), list(), deque()

    queue.append(node)

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.pop(0)
            if is_a_leaf(current_node):
                continue
            elif i == 0:
                left_children.append(current_node.val)
            elif i == level_size - 1:
                right_children.appendleft(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    leaves = find_leaves_dfs(node)
    return left_children + list(leaves) + list(right_children)


def find_leaves_dfs(node: TreeNode):
    leaves = list()
    queue = list()
    queue.append(node)

    while queue:
        current_node = queue.pop()
        if is_a_leaf(current_node):
            leaves.append(current_node.val)
        if current_node.right:
            queue.append(current_node.right)
        if current_node.left:
            queue.append(current_node.left)
    return leaves


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(9)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(15)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)

    print(find_tree_boundary(root))
