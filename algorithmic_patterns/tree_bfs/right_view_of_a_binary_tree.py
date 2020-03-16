"""
Return the right view of the binary tree
"""


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def right_side_of_the_tree(root: TreeNode):
    if not root:
        return []

    queue, result = list(), list()

    queue.append(root)

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.pop()
            if i == level_size - 1:
                result.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
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

    print(right_side_of_the_tree(n1))