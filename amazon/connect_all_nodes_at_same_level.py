"""
Given a k-ary tree connect all nodes at a given level
"""

from typing import List, Dict

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        return '{}: {}'.format(self.data, self.children)


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}'.format(self.data)


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if not self.head:
            self.head = ListNode(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(data)

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '->'.join(nodes)


def update_levels_dict(root: TreeNode, levels: Dict, level_number: int) -> None:
    if level_number not in levels:
        levels[level_number] = list()
    levels[level_number].append(root.data)
    for child in root.children:
        update_levels_dict(child, levels, level_number + 1)


def build_singly_linked_list_from(arr: List[int]) -> SinglyLinkedList:
    singly_linked_list = SinglyLinkedList()
    for element in arr:
        singly_linked_list.append(element)
    return singly_linked_list


def connect_nodes_at_same_level(root: TreeNode):
    levels = dict()
    update_levels_dict(root, levels, 0)
    for level in levels:
        arr = levels[level]
        print(build_singly_linked_list_from(arr))


if __name__ == '__main__':
    a = TreeNode(4)
    b = TreeNode(3)
    c = TreeNode(9)
    d = TreeNode(5)
    e = TreeNode(3)
    f = TreeNode(9)

    b.children = [c]
    e.children = [f]
    a.children = [b, d, e]

    print(connect_nodes_at_same_level(a))