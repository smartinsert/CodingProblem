"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
"""

import math


def minimum_window_sort(arr):
    low, high = 0, len(arr) - 1
    while low < len(arr) and arr[low] <= arr[low + 1]:
        low += 1

    if low == len(arr) - 1:
        return 0

    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    subarray_max = -math.inf
    subarray_min = math.inf

    for k in range(low, high+1):
        subarray_max = max(subarray_max, arr[k])
        subarray_min = min(subarray_min, arr[k])

    while low > 0 and arr[low-1] > subarray_min:
        low -= 1

    while high < len(arr) - 1 and arr[high+1] < subarray_max:
        high += 1

    return high - low + 1


if __name__ == '__main__':
    print(minimum_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))