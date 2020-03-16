"""
Find the level order successor of a given node
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.left.data}<-{self.data}->{self.right.data}'


def level_order_successor(root: TreeNode, key: TreeNode):
    if not root:
        return None
    queue = list()

    queue.append(root)

    return_successor = False
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.pop(0)
            if return_successor:
                return current_node.data
            if current_node.data == key.data:
                return_successor = True
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    return None


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

    print(level_order_successor(n1, n3))