class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def validate_tree(bin_tree):
    return validate_tree_node(bin_tree, -float('inf'), float('inf'))


def validate_tree_node(node, left_bound, right_bound):
    if not node:
        return True
    return left_bound <= node <= right_bound and \
           validate_tree_node(node.left, left_bound, node.data) and \
           validate_tree_node(node.right, node.data, right_bound)
