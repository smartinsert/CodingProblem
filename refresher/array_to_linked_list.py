"""
Convert an array to a linked list
"""

from typing import List


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return '{}'.format(self.data)


class SinglyLinkedList:
    def __init__(self, node=None):
        self. head = node

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '->'.join(nodes)


def array_to_linked_list(input_arr: List[int]):
    pass


if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.add(2)
    sll.add(3)
    sll.add(4)
    print(sll)