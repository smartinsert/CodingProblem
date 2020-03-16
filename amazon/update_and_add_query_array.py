"""
Given an array arr[0..n-1]. The following operations need to be performed.

update(l, r, val) : Add ‘val’ to all the elements in the array from [l, r].
getElement(i) : Find element in the array indexed at ‘i’.
Initially all the elements in the array are 0. Queries can be in any order, i.e., there can be many updates before
point query.
"""


class Array:
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)
        self.binary_index_tree = [0] * (self.length + 1)
        self.__construct_bi_tree()

    def __construct_bi_tree(self):
        for i in range(self.length):
            self.__update_bit(i, self.arr[i])

    def __update_bit(self, index, value):
        index += 1
        while index <= self.length:
            self.binary_index_tree[index] += value
            index += index & (-index)

    def __get_sum(self, index):
        summ = 0
        index += 1
        while index > 0:
            summ += self.binary_index_tree[index]
            index -= index & (-index)
        return summ

    def update_using_prefix_sum(self, left, right, value):
        self.arr[left] += value
        if right + 1 < self.length:
            self.arr[right + 1] -= value

    def update_using_bi_tree(self, left, right, value):
        self.__update_bit(left, value)
        self.__update_bit(right, -value)

    def get_element_using_bit(self, index):
        return self.__get_sum(index)

    def get_element_prefix_sum(self, index):
        summ = 0
        for i in range(index+1):
            summ += self.arr[i]
        return summ


if __name__ == '__main__':
    array = Array([0, 0, 0, 0, 0])
    array.update_using_prefix_sum(0, 4, 2)
    print(array.get_element_prefix_sum(3))

    array.update_using_prefix_sum(3, 4, 3)
    print(array.get_element_prefix_sum(3))

    array.update_using_bi_tree(0, 4, 2)
    print(array.get_element_using_bit(3))

    array.update_using_bi_tree(3, 4, 3)
    print(array.get_element_using_bit(3))