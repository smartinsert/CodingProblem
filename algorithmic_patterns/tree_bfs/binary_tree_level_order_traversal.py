"""
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.left.data}<-{self.data}->{self.right.data}'


def level_order_traversal(node: TreeNode):
    result = []
    if not node:
        return result
    queue = list()
    queue.append(node)

    while queue:
        level_size = len(queue)
        current_level = list()
        for _ in range(level_size):
            current_node = queue.pop(0)
            current_level.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)
    return result


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7

    print(level_order_traversal(n1))