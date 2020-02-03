"""
Given an array of integers, find and print the minimum absolute difference between any two elements in the array.
"""

from typing import List


def minimum_absolute_difference(arr: List[int]) -> float:
    arr.sort()
    return min(abs(x-y) for x, y in zip(arr, arr[1:]))


if __name__ == '__main__':
    assert minimum_absolute_difference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]) == 1