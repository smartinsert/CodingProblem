"""
Arrange given numbers to form the biggest number
"""

import functools
from itertools import permutations
# Python3 Program to get the maximum
# possible integer from given array
# of integers...


# custom comparator to sort according
# to the ab, ba as mentioned in description
def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return (int(ab) < int(ba)) - (int(ab) > int(ba))


def largest(l):
    lst = []
    for i in permutations(l, len(l)):
        # provides all permutations of the list values,
        # store them in list to find max
        lst.append("".join(map(str, i)))
    return max(lst)


# driver code
if __name__ == "__main__":
    a = [54, 546, 548, 60, ]
    # sorted_array = sorted(a, key=my_compare(comparator))
    sorted_array = sorted(a, key=functools.cmp_to_key(comparator))
    number = "".join([str(i) for i in sorted_array])
    print(number)