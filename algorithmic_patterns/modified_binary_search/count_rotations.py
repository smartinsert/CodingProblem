"""
Count the number of rotations of the sorted array

The pivot is the only element which is less than it's previous element. The index of the smallest element is the
number of rotations.
"""


def count_rotations(arr):
    if len(arr) == 0:
        return 0
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid
        # Check which side is sorted
        if arr[start] < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


if __name__ == '__main__':
    print(count_rotations([10, 15, 1, 3, 8]))