"""
Write a program to find the element whose index is equal to itself in a sorted array
"""

from typing import List


def find_element(arr: List[int], low=0, high=0) -> int:
    mid = (low + high) // 2
    if arr[mid] == mid:
        return mid
    if arr[mid] < mid:
        return find_element(arr, low, mid)
    elif arr[mid] > mid:
        return find_element(arr, mid, high)


if __name__ == '__main__':
    print(find_element([1, 2, 2, 3], 0, 4))
    print(find_element([1, 2, 3, 3, 4], 0, 5))