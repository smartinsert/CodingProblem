"""
Given a binary tree, return the zigzag traversal
"""
from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.left.data}<-{self.data}->{self.right.data}'


def zigzag_traversal(node: TreeNode):
    if not node:
        return []
    result, queue = list(), list()

    queue.append(node)

    left_to_right = True
    while queue:
        level_size = len(queue)
        current_level = deque()
        for i in range(level_size):
            current_node = queue.pop(0)
            if left_to_right:
                current_level.append(current_node.data)
            else:
                current_level.appendleft(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(list(current_level))
        left_to_right = not left_to_right
    return result


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7

    print(zigzag_traversal(n1))