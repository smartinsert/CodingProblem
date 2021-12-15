"""
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
"""

from algorithmic_patterns.fast_and_slow_pointers import Node


def is_palindromic_linked_list(head: Node) -> bool:
    if head is None or head.next is None:
        return True
    fast, slow = None, None
    if head is not None:
        fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    second_half_head = reverse(slow)
    copy_of_second_half_head = second_half_head
    while head is not None and second_half_head is not None:
        if head.value != second_half_head.value:
            return False
        head, second_half_head = head.next, second_half_head.next
    reverse(copy_of_second_half_head)

    if head is None and second_half_head is None:
        return True
    return False


def reverse(head: Node):
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
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

