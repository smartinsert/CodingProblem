"""
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an
index smaller than i.

More formally,
G[i] for an element A[i] = an element A[j] such that j is maximum possible AND j < i AND A[j] < A[i]

Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]
"""

import math


def nearest_smallest_element(arr):
    n = len(arr)
    result = [0 for _ in range(n)]
    if n == 0:
        return result

    result[0] = -1
    min_till_now, min_idx = math.inf, 0
    for i in range(1, len(arr)):
        if arr[i] < min_till_now:
            min_till_now = arr[i]
            min_idx = i
        for j in range(i):
            if arr[j] < arr[i] and i-j == 1:
                result[i] = arr[j]
            elif arr[j] > min_till_now and j > min_idx:
                result[i] = min_till_now
            else:
                result[i] = -1
    return result


if __name__ == '__main__':
    print(nearest_smallest_element([4, 5, 2, 10, 8]))
    print(nearest_smallest_element([3, 2, 1]))
