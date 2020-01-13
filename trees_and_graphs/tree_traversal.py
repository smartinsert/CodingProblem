class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order_iterative(root):
    result = list()
    if not root:
        return result
    stack = list()
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.value)
        root = root.right
    return result


def in_order_recursive(root, result=None):
    if root is None:
        return list()
    if result is None:
        result = list()
    in_order_recursive(root.left, result)
    result.append(root.value)
    in_order_recursive(root.right, result)
    return result


def pre_order(root, result=None):
    if root is None:
        return list()
    if result is None:
        result = list()
    result.append(root.value)
    pre_order(root.left, result)
    pre_order(root.right, result)
    return result


def post_order(root, result=None):
    if root is None:
        return list()
    if result is None:
        result = list()
    post_order(root.left, result)
    post_order(root.right, result)
    result.append(root.value)
    return result


if __name__ == '__main__':
    n1 = Node(100)
    n2 = Node(50)
    n3 = Node(150)
    n4 = Node(25)
    n5 = Node(75)
    n6 = Node(125)
    n7 = Node(175)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    assert in_order_recursive(n1) == [25, 50, 75, 100, 125, 150, 175]
    assert pre_order(n1) == [100, 50, 25, 75, 150, 125, 175]
    assert post_order(n1) == [25, 75, 50, 125, 175, 150, 100]