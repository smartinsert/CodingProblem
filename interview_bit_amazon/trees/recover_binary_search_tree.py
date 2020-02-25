"""
Two elements of a binary search tree (BST) are swapped by mistake.
Tell us the 2 values swapping which the tree will be restored.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_traversal(node: TreeNode, result):
    if not node:
        return result
    in_order_traversal(node.left, result)
    result.append(node.data)
    in_order_traversal(node.right, result)


def get_nodes_to_swap(in_order_traversal):
    nodes_to_swap, candidates = [], []
    n = len(in_order_traversal)
    if n == 0:
        return nodes_to_swap
    for i in range(1, len(in_order_traversal) - 1):
        if in_order_traversal[i] < in_order_traversal[i-1]:
            candidates.append((in_order_traversal[i-1], in_order_traversal[i]))
    if len(candidates) == 2:
        nodes_to_swap.append(candidates[0][0])
        nodes_to_swap.append(candidates[1][1])
    elif len(candidates) == 1:
        nodes_to_swap.append(candidates[1])
        nodes_to_swap.append(candidates[0])
    return nodes_to_swap


def get_nodes_to_swap_better(node: TreeNode, first_start_point, last_end_point, prev_node):
    if not node:
        return

    get_nodes_to_swap_better(node.left, first_start_point, last_end_point, prev_node)

    if prev_node is not None:
        if prev_node.data > node.data:
            if first_start_point is None:
                first_start_point = prev_node
            last_end_point = node
    prev_node = node

    get_nodes_to_swap_better(node.right, first_start_point, last_end_point, prev_node)


def recover_tree(node: TreeNode):
    first_start_point, last_end_point, prev_node = None, None, None
    get_nodes_to_swap_better(node, first_start_point, last_end_point, prev_node)
    return [first_start_point.data, last_end_point.data]

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.left = node2
    node1.right = node3

    # nodes_to_swap = []
    # pre_order_traversal(node1, nodes_to_swap)
    # print(nodes_to_swap)

    node4 = TreeNode(10)
    node5 = TreeNode(5)
    node6 = TreeNode(15)
    node7 = TreeNode(4)
    node8 = TreeNode(7)
    node9 = TreeNode(14)
    node10 = TreeNode(17)

    node4.left, node4.right = node6, node5
    node6.left, node6.right = node7, node8
    node5.left, node5.right = node9, node10

    result = []
    in_order_traversal(node4, result)
    nodes_to_swap = get_nodes_to_swap(result)
    print(nodes_to_swap)

    print(recover_tree(node4))





