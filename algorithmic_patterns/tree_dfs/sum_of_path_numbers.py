"""
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
Find the total sum of all the numbers represented by all paths.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.left.data}<-{self.data}->{self.right.data}'


def total_sum(node: TreeNode):
    all_paths = []
    find_all_path_sum(node, all_paths, [])
    return sum([int(i) for i in all_paths])


def find_all_path_sum(node, all_paths, current_path):
    if not node:
        return

    current_path.append(node.data)

    find_all_path_sum(node.left, all_paths, current_path)
    find_all_path_sum(node.right, all_paths, current_path)

    all_paths.append(list(current_path))

    del current_path[-1]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print(total_sum(root))