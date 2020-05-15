"""
Find the smallest number index in the array greater than or equal to the key
"""


# Time: O(logN)
def smallest_number_greater_than(arr, key):
    n = len(arr)
    if n == 0 or key > arr[n-1]:
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
    return start