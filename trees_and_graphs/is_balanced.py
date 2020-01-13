"""
O(N^2) solution
"""


def check_height(root):
    if root is None:
        return 0
    return max(check_height(root.left), check_height(root.right)) + 1


def is_tree_balanced(root):
    if root is None:
        return 0
    left_height = check_height(root.left)
    right_height = check_height(root.right)
    if abs(right_height - left_height) > 1:
        return -1
    else:
        return is_tree_balanced(root.left) and is_tree_balanced(root.right)

"""
O(N) solution
"""


def is_balanced(root):
    return __is_balanced_recursive(root)


def __is_balanced_recursive(root):
    return -1 != __get_depth(root)


def __get_depth(root):
    if root is None:
        return 0
    left = __get_depth(root.left)
    right = __get_depth(root.right)
    if abs(right - left) > 1 or -1 in [left, right]:
        return -1
    return 1 + max(left, right)

