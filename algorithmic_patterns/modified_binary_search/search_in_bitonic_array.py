"""
Seach in a bitonic array
"""


def search(arr, key):
    max_idx = find_max(arr)
    key_idx = binary_search(arr, 0, max_idx, key)
    if key_idx != -1:
        return arr[key_idx]
    return binary_search(arr, max_idx+1, len(arr)-1, key)


# O(logN)
def find_max(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid+1]:
            end = mid
        else:
            start = mid + 1
    return start


# O(logN)
def binary_search(arr, left, right, key):
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        if arr[left] < arr[right]: # ascending order
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        if arr[left] > arr[right]: # descending order
            if arr[mid] < key:
                right = mid - 1
            else:
                left = mid + 1
    return -1