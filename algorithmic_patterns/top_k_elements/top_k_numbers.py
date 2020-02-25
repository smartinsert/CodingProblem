"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
Input: [3, 1, 5, 12, 2, 11], K = 3

Add to max heap and pop k times.

transformed array: [-3, -1, -5, -12, -2, -11]
"""

from heapq import *


def top_k_numbers(arr, k):
    k_top_numbers = []
    min_heap = []
    if not arr:
        return k_top_numbers
    for i in range(k):
        min_heap.append(arr[i])

    for i in range(k, len(arr)):
        if arr[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, arr[i])
    k_top_numbers = [heappop(min_heap) for _ in range(k)]
    return k_top_numbers


if __name__ == '__main__':
    print(top_k_numbers([3, 1, 5, 12, 2, 11], 3))