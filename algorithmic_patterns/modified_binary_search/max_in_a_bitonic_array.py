"""
Find max in a bitonic array
Time: O(logN)
"""


def find_max(arr):
    if len(arr) == 0:
        return -1
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return arr[start]


if __name__ == '__main__':
    print(find_max([1, 3, 8, 12, 4, 2]))