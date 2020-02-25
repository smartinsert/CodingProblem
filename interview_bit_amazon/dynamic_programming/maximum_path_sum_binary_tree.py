"""
Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.
"""

import math

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_maximum_sum(root: Node):
    """
    There are three ways to get the maximum sum
    1. Max sum including the left children and the root
    2. Max sum including the right children and the root
    3. Max path sum of left + root + Math path sum of right
    """
    if not root:
        return 0

    left_child_sum = find_maximum_sum(root.left)
    right_child_sum = find_maximum_sum(root.right)

    # Max including at most one child
    max_single = max(max(left_child_sum, right_child_sum) + root.data, root.data)

    # Max including both children and the root
    max_top = max(max_single, left_child_sum + right_child_sum + root.data)

    find_maximum_sum.result = max(find_maximum_sum.result, max_top)

    return max_single


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    find_maximum_sum.result = -math.inf
    find_maximum_sum(root)
    print(find_maximum_sum.result)
