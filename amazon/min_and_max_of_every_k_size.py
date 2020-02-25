"""
Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.
"""
import math


def find_max(arr):
    max_here = -math.inf
    for i in arr:
        max_here = max(max_here, i)
    return max_here


def min_max(arr, k):
    if len(arr) < k:
        return []

    window_start, window_end = 0, 0
    result = []

    for window_end in range(len(arr)):
        if (window_end - window_start + 1) == k:
            result.append(find_max(arr[window_start:window_end+1]))
            window_start += 1
    return result


if __name__ == '__main__':
    print(min_max([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))