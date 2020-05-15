"""
Find the element in a sorted array that has a least difference from the key
"""


def find_the_minimum_difference_element(arr, key):
    n = len(arr)
    if n == 0 or key >= arr[n-1]:
        return -1

    start, end = 0, n - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            return mid

    if arr[start] - key < arr[end] - key:
        return arr[start]
    return arr[end]