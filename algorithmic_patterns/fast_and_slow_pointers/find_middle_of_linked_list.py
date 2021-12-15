"""
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Example 1:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3
Example 2:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4
Example 3:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4
"""

from algorithmic_patterns.fast_and_slow_pointers import Node


def find_middle(head: Node) -> Node:
    if head is None:
        return head
    slow, fast = None, None
    if head is not None:
        slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Middle Node: " + str(find_middle(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle(head).value))

