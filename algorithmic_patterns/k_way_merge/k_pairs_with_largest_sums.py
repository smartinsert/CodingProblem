"""
Find k pairs with largest sum in two lists
"""

from heapq import *


def k_pairs_with_largest_sum(nums_1, nums_2, k):
    if len(nums_1) == 0 and len(nums_2) == 0:
        return []
    min_heap, result = [], []

    for i in range(len(nums_1)):
        for j in range(len(nums_2)):
            if len(min_heap) < k:
                heappush(min_heap, (nums_1[i] + nums_2[j], i, j))
            else:
                if nums_1[i] + nums_2[j] < min_heap[0][0]:
                    break
                else:
                    heappop(min_heap)
                    heappush(min_heap, (nums_1[i] + nums_2[j], i, j))

    for summ, i, j in range(len(min_heap)):
        result.append([nums_1[i], nums_2[j]])
    return result

