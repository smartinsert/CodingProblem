"""
Given the head of a LinkedList with a cycle, find the length of the cycle.
"""

class Node:
    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next


def length_of_the_cycle(head: Node):
    if head is None:
        return 0
    fast, slow = None, None
    if head is not None:
        fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return calculate_cycle_length(slow)
    return 0


def calculate_cycle_length(slow: Node):
    current = None
    cycle_length = 0
    if slow is not None:
        current = slow
    while True and current is not None:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next

    print(length_of_the_cycle(head))

    head.next.next.next.next.next.next = head.next.next.next

    print(length_of_the_cycle(head))




