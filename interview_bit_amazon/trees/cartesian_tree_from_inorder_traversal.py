"""
Given an inorder traversal of a cartesian tree, construct the tree.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_in_order(node: TreeNode):
    if node:
        print_in_order(node.left)
        print(node.data)
        print_in_order(node.right)


def build_tree(in_order, start, end):
    if start > end:
        return None

    max_idx = get_max_index(in_order, start, end)

    node = TreeNode(in_order[max_idx])

    if start == end:
        return node

    node.left = build_tree(in_order, start, max_idx - 1)

    node.right = build_tree(in_order, max_idx + 1, end)

    return node


def get_max_index(in_order, start, end):
    maximum = inorder[start]
    max_idx = start
    for i in range(start + 1, end+1):
        if in_order[i] > maximum:
            max_idx = i
            maximum = inorder[i]
    return max_idx


if __name__ == '__main__':
    inorder = [5, 10, 40, 30, 28]
    print_in_order(build_tree(inorder, 0, len(inorder) - 1))
