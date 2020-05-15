"""
Find the max path sum in a binary tree
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time: O(n); Space: O(logN)
def max_path_sum(root: TreeNode):
    if not root:
        return 0, 0

    left_max_branch_sum, left_max_sum = max_path_sum(root.left)
    right_max_branch_sum, right_max_sum = max_path_sum(root.right)

    max_child_path_sum_as_branch = max(left_max_branch_sum, right_max_branch_sum)

    value = root.value

    max_path_sum_as_branch = max(max_child_path_sum_as_branch + value, value)

    max_path_sum_as_root_node = max(left_max_branch_sum + value + right_max_branch_sum, max_path_sum_as_branch)

    running_path_sum = max(left_max_sum, right_max_sum, max_path_sum_as_root_node)

    return max(running_path_sum, max_path_sum_as_branch)