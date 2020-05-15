"""
search in a sorted infinite array with a given reader
"""

import math


class Reader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_key(reader: Reader, key: int):
    start, end = 0, 1

    while reader.get(end) < key:
        new_start = end + 1
        end = (end - start + 1) * 2
        start = new_start
    return binary_search(start, end, reader, key)


def binary_search(start, end, reader, key):
    while start <= end:
        mid = start + (end- start) // 2
        if reader.get(mid) > key:
            end = mid - 1
        elif reader.get(mid) < key:
            start = mid + 1
        else:
            return mid
    return -1