"""
Arrange given numbers to form the biggest number
"""


# Python3 Program to get the maximum
# possible integer from given array
# of integers...


# custom comparator to sort according
# to the ab, ba as mentioned in description
def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return (int(ba) > int(ab)) - (int(ba) < int(ab))


def my_compare(custom_comparator):
    # Convert a cmp= function into a key= function
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return custom_comparator(self.obj, other.obj) < 0

        def __gt__(self, other):
            return custom_comparator(self.obj, other.obj) > 0

        def __eq__(self, other):
            return custom_comparator(self.obj, other.obj) == 0

        def __le__(self, other):
            return custom_comparator(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return custom_comparator(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return custom_comparator(self.obj, other.obj) != 0

    return K


from itertools import permutations


def largest(l):
    lst = []
    for i in permutations(l, len(l)):
        # provides all permutations of the list values,
        # store them in list to find max
        lst.append("".join(map(str, i)))
    return max(lst)


print(largest([54, 546, 548, 60]))

# driver code
if __name__ == "__main__":
    a = [54, 546, 548, 60, ]
    sorted_array = sorted(a, key=my_compare(comparator))
    number = "".join([str(i) for i in sorted_array])
    print(number)