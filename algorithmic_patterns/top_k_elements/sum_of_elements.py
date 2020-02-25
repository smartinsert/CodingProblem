"""
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.
"""

from heapq import *


def sum_of_numbers_between(arr, k1, k2):
    if len(arr) == 0:
        return 0
    if k1 > len(arr) or k2 > len(arr):
        return 0
    min_heap = []
    elements_sum = 0
    for i in range(len(arr)):
        heappush(min_heap, arr[i])

    for i in range(k1):
        heappop(min_heap)

    for i in range(k2-k1-1):
        elements_sum += heappop(min_heap)

    return elements_sum


if __name__ == '__main__':
    print(sum_of_numbers_between([1, 3, 12, 5, 15, 11], 3, 6))
    print(sum_of_numbers_between([3, 5, 8, 7], 1, 4))