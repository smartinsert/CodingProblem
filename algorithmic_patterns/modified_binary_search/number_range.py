"""
Find the start and end indices of a key in a sorted array with duplicate elements
"""


def number_range(arr, key):
    n = len(arr)
    result = [-1, -1]
    if n == 0 or key > arr[n-1]:
        return result
    result[0] = binary_search(arr, 0, n-1, key, False)
    if result[0] != -1:
        result[1] = binary_search(arr, 0, n-1, key, True)
    return result


def binary_search(arr, start, end, key, find_max_idx):
    key_index = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            key_index = mid
            if find_max_idx:
                start = mid + 1
            else:
                end = mid - 1
    return key_index