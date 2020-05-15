"""
Merge k sorted list
"""

from heapq import *


def merge_k_sorted_list(*klists):
    heap = []
    result = []
    for i in range(len(klists)):
        heappush(heap, (klists[i][0], 0, klists[i]))

    while heap:
        number, i, lst = heappop(heap)
        result.append(number)

        if len(lst) > i + 1: # if the array of the top element has more elements add it's next element to the heap
            heappush(heap, (lst[i+1], i + 1, lst))
    return result


if __name__ == '__main__':
    print(merge_k_sorted_list([2, 6, 8], [3, 6, 7], [1, 3, 4]))