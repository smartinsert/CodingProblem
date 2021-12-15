from python_data_structures.linked_list import LinkedList


def reverse(lst):
    if lst.is_empty():
        return lst

    prev, current = None, lst.get_head()

    while current is not None:
        next = current.next_element
        current.next_element = prev
        prev = current
        current = next
    return prev


lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
lst.head_node = reverse(lst)
lst.print_list()
