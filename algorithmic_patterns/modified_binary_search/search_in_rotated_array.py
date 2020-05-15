"""
Search in a rotated array
Time: O(logN)
"""


def search_in_a_rotated_array(arr, key):
    if len(arr) == 0:
        return -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        if arr[start] <= arr[mid]:
            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:  # right side is in ascending order
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == '__main__':
    print(search_in_a_rotated_array([10, 15, 1, 3, 8], 15))
