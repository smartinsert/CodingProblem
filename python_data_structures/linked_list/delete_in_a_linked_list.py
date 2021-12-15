"""
Delete a value in a linked list
"""
from python_data_structures.linked_list import LinkedList


def delete(lst: LinkedList, value) -> bool:
    if lst.get_head() is None:
        return False
    prev, current = lst.get_head(), lst.get_head()
    while current is not None:
        prev = current
        current = current.next_element
        if current.data == value:
            prev.next_element = current.next_element
            current.next_element = None
            return True
    return False


lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
delete(lst, 4)
lst.print_list()