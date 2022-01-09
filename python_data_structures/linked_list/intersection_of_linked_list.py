"""
Given two lists, find if they intersect. That is, they have the same address
"""
from python_data_structures.linked_list import LinkedList


def do_intersect(l1: LinkedList, l2: LinkedList) -> bool:
    if l1.is_empty() or l2.is_empty():
        return False
    head1 = l1.get_head()
    head2 = l2.get_head()
    copy_of_head2 = head2
    if head1 is head2:
        return head1
    while head2 and head1:
        while copy_of_head2:
            if copy_of_head2.next_element:
                copy_of_head2 = copy_of_head2.next_element
                if copy_of_head2 == head1:
                    return head1
            else:
                copy_of_head2 = copy_of_head2.next_element
        copy_of_head2 = head2.next_element
        head1 = head1.next_element
    return None


# lst1 = LinkedList()
# lst2 = LinkedList()
#
#
# lst1.insert_at_head(4)
# lst1.insert_at_head(13)

# lst.insert_at_head(7)
# lst.insert_at_head(22)
# lst.insert_at_head(14)
# lst.insert_at_head(21)
# lst.insert_at_head(14)
# lst.insert_at_head(7)


def find_happy_number(num):
    if num == 1:
        return True
    fast, slow = num, num
    while True:
        fast = find_square_and_sum(find_square_and_sum(fast))
        slow = find_square_and_sum(slow)
        if fast == slow:
            return slow == 1


def find_square_and_sum(number):
    _sum = 0
    while number:
        digit = number % 10
        _sum += digit * digit
        number //= 10
    return _sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
