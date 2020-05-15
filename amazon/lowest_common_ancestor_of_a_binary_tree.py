"""
Find the lowest common ancestor of a binary tree
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root: TreeNode, node_1, node_2):
    path_1 = []
    path_2 = []

    if not find_path(root, node_1, path_1) or not find_path(root, node_2, path_2):
        return -1

    i = 0
    while i < len(path_1) and i < len(path_2):
        if path_1[i] != path_2[i]:
            break
        i += 1
    return path_1[i-1]


def find_path(root: TreeNode, node_to_find: TreeNode, path_to_node):
    if not root:
        return False

    path_to_node.append(root.value)

    if node_to_find == root.value:
        return True

    if (root.left and find_path(root.left, node_to_find, path_to_node)) or \
            (root.right and find_path(root.right, node_to_find, path_to_node)):
        return True

    # If not present in the current root, remove the root
    path_to_node.pop()
    return False
