"""
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of
each path equals ‘S’.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.left.data}<-{self.data}->{self.right.data}'


def find_all_paths(node: TreeNode, target_sum):
    all_paths = []
    find_all_path_recursive(node, target_sum, [], all_paths)
    return all_paths


def find_all_path_recursive(node, target_sum, current_path, all_paths):
    if not node:
        return

    current_path.append(node.data)

    if not node.left and not node.right and node.data == target_sum:
        all_paths.append(list(current_path))
    else:
        find_all_path_recursive(node.left, target_sum - node.data, current_path, all_paths)
        find_all_path_recursive(node.right, target_sum - node.data, current_path, all_paths)

    # remove the current node from the path to backtrack while going up the recursive call stack
    del current_path[-1]


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    target_sum = 23
    print(find_all_paths(root, target_sum))