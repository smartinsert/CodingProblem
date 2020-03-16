"""
Given a binary tree, find the level order averages
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.left.data}<-{self.data}->{self.right.data}'


def level_order_averages(node: TreeNode):
    if not node:
        return []
    result, queue = [], []

    queue.append(node)

    while queue:
        level_size = len(queue)
        level_sum = 0
        for i in range(level_size):
            current_node = queue.pop(0)
            level_sum += current_node.data
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        level_average = level_sum/level_size
        result.append(level_average)
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
    
    print(level_order_averages(n1))