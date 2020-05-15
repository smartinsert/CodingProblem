"""
Find all possible bsts given nodes from 1 to n
Time: O(n*2^n)
Space: O(2^n)
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_all_possible_bsts(n):
    if n <= 0:
        return []
    return find_all_possible_bsts_recursive(1, n)


def find_all_possible_bsts_recursive(start, end):
    result = []
    if start > end:
        result.append(None)
        return result

    for i in range(start, end+1):
        left_subtrees = find_all_possible_bsts_recursive(start, i-1)
        right_subtrees = find_all_possible_bsts_recursive(i, end)

        for left_subtree in left_subtrees:
            for right_subtree in right_subtrees:
                root = TreeNode(i)
                root.left = left_subtree
                root.right = right_subtree
                result.append(root)
    return result
