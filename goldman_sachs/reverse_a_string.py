"""
Given an array (or string), the task is to reverse the array/string.
"""

from typing import List


def reverse_a_string(arr: List[int]) -> List[int]:
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def reverse_string_recursive(arr: List[int], start: int, end: int) -> List[int]:
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_string_recursive(arr, start + 1, end - 1)


if __name__ == '__main__':
    print(reverse_a_string([4, 5, 1, 2]))
    print(reverse_string_recursive([4, 5, 1, 2], 0, 3))