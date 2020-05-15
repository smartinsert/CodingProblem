"""
Find the kth smallest number in m sorted list
"""

from heapq import *


def kth_smallest_number_in_m_sorted_list(*args):
    k = args[0]
    heap = []

    lists = args[1:][0]
    for i in range(len(lists)):
         heappush(heap, (lists[i][0], 0, lists[i]))

    number_count, number = 0, 0

    while heap:
        number, idx, lst = heappop(heap)
        number_count += 1
        if number_count == k:
            break
        if len(lst) > idx + 1:
            heappush(heap, (lst[idx+1], idx + 1, lst))
    return number


if __name__ == '__main__':
    print(kth_smallest_number_in_m_sorted_list(5, [[2, 6, 8], [3, 6, 7], [1, 3, 4]]))