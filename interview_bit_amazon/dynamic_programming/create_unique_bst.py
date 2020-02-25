"""
Construct all possible BSTs for keys 1 to N
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root: TreeNode):
    if root is not None:
        print(root.value)
        preorder(root.left)
        preorder(root.right)


def construct_trees(start, end):
    all_trees = []
    if start > end:
        all_trees.append(None)
        return all_trees

    for i in range(start, end+1):
        left_subtree = construct_trees(start, i)
        right_subtree = construct_trees(i+1, end)

        for j in range(len(left_subtree)):
            left = left_subtree[i]
            for k in range(len(right_subtree)):
                right = right_subtree[k]
                node = TreeNode(i)
                node.left = left
                node.right = right




