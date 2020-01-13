class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + ',' + str(self.next)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        if not self.head:
            self.head = self.tail = ListNode(item)
        else:
            self.tail.next = ListNode(item)
            self.tail = self.tail.next

    def remove(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.depth = None


def list_of_depths(binary_tree):
    if not binary_tree:
        return list()
    lists = list()
    tail = None
    root = binary_tree
    queue = Queue()
    depth = -1
    root.depth = 0
    while root:
        if root.depth == depth:
            tail.next = ListNode(root.data)
            tail = tail.next
        else:
            depth = root.depth
            tail = ListNode(root.data)
            lists.append(tail)
        for child in (root.left, root.right):
            if child:
                child.depth = root.depth + 1
                queue.add(child)
        root = queue.remove()
    return lists


if __name__ == '__main__':
    node_h = TreeNode('H')
    node_g = TreeNode('G')
    node_f = TreeNode('F')
    node_e = TreeNode('E', node_g)
    node_d = TreeNode('D', node_h)
    node_c = TreeNode('C', None, node_f)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)
    lists = list_of_depths(node_a)
