class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def reverse_linked_list(head):
    if not head or not head.next:
        return head
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev