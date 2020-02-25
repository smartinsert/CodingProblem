"""
Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost.
The cost of connecting two ropes is equal to the sum of their lengths.
"""

from heapq import *


def cost_to_connect_ropes(rope_sizes):
    if not rope_sizes:
        return 0
    min_heap = []
    for i in range(len(rope_sizes)):
        heappush(min_heap, rope_sizes[i])

    result = 0
    while len(min_heap) > 1:
        first_rope_length = heappop(min_heap)
        second_rope_length = heappop(min_heap)
        result += first_rope_length + second_rope_length
        heappush(min_heap, first_rope_length + second_rope_length)
    return result


if __name__ == '__main__':
    print(cost_to_connect_ropes([1, 3, 11, 5]))