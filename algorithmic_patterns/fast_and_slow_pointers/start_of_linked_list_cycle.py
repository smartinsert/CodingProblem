"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""
from algorithmic_patterns.fast_and_slow_pointers import Node


def start_of_linked_list_cycle(head: Node) -> Node:
    if head is None:
        return head
    fast, slow = None, None
    if head is not None:
        fast, slow = head, head
    first_pointer, second_pointer = head, None
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            second_pointer = compute_cycle_length(slow)
            break
    while first_pointer != second_pointer:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    return second_pointer


def compute_cycle_length(slow: Node):
    current, cycle_length = None, 0
    if slow is not None:
        current = slow
    while True and current is not None:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return current


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(start_of_linked_list_cycle(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(start_of_linked_list_cycle(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(start_of_linked_list_cycle(head).value))





