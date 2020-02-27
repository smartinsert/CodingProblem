"""
Return the number of adjacent swaps required to sort the array
"""

from typing import List


def count_swaps(arr: List[int]) -> int:
    # Number of swaps would be equal to the number of inversions in the array
    temp_arr = [0 for _ in range(len(arr))]
    return merge_sort(arr, temp_arr, 0, len(arr) - 1)


def merge(arr, temp, low, mid, high):
    i = low
    j = mid
    k = low
    inversion_count = 0
    while i <= mid - 1 and j <= high:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            inversion_count += mid - i
            j += 1
            k += 1
    while i <= mid - 1:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(len(arr)):
        arr[i] = temp[i]

    return inversion_count


def merge_sort(arr, temp_arr, low, high):
    inversion_count = 0
    if low < high:
        mid = (low + high) // 2
        inversion_count = merge_sort(arr, temp_arr, low, mid)
        inversion_count += merge_sort(arr, temp_arr, mid + 1, high)
        inversion_count += merge(arr, temp_arr, low, mid + 1, high)
    return inversion_count


if __name__ == '__main__':
    print(count_swaps([1, 20, 6, 4, 5]))

