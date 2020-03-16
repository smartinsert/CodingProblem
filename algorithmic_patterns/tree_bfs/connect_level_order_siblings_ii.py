"""
Given a binary tree, connect each node with its level order successor. The last node of each level should point to
the first node of the next level.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next_node = None

    def print_level_order(self):
        next_level_root = self
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                print(f'{current.data}', sep='->')
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next_node
            print()


def connect_all_siblings(root: TreeNode):
    if not root:
        return

    queue = list()

    queue.append(root)

    previous_node = None
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.pop(0)
            if previous_node:
                previous_node.next_node = current_node
            previous_node = current_node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    print(previous_node.data, ' ', previous_node.next_node)


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    connect_all_siblings(root)
    root.print_level_order()