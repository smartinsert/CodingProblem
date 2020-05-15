"""
Find the smallest range with atleast one number from each sorted list
"""

from heapq import *
import math


def find_smallest_range(lists):
    if len(lists) == 0:
        return []

    range_start, range_end = 0, math.inf
    current_max_number = -math.inf
    min_heap = []

    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))
        current_max_number = max(current_max_number, lists[i][0])

    while len(min_heap) == len(lists):
        number, idx, lst = heappop(min_heap)

        if range_end - range_start > current_max_number - number:
            range_start = number
            range_end = current_max_number

        if len(lst) > idx + 1:
            heappush(min_heap, (lst[idx + 1], idx + 1, lst))
            current_max_number = max(current_max_number, lst[idx + 1])
    return [range_start, range_end]


if __name__ == '__main__':
    print(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]]))