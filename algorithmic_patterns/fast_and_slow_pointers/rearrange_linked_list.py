"""
Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

Example 1:

Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null
Example 2:

Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
"""
from algorithmic_patterns.fast_and_slow_pointers import Node


def reorder(head: Node) -> None:
    if head is None or head.next is None:
        return
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    head_second_half = reverse(slow)
    head_first_half = head

    while head_first_half is not None and head_second_half is not None:
        first_half_next_head = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = first_half_next_head

        second_half_next_head = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = second_half_next_head

    if head_first_half is not None:
        head_first_half.next = None


def reverse(head: Node) -> Node:
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()
