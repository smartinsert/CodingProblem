"""
There are N couples sitting in a row of length 2 * N. They are currently ordered randomly,
but would like to rearrange themselves so that each couple's partners can sit side by side.
"""
from typing import List


def minimum_swaps(arrangement: List[int]) -> int:
    arrangement_position = [*enumerate(arrangement)]
    arrangement_position.sort(key=lambda x: x[1])
    visited = [False for _ in range(len(arrangement))]
    number_of_swaps = 0
    for i in range(len(arrangement) - 1):
        if visited[i] or (arrangement_position[i][0] == i and arrangement_position[i+1][0] == i):
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arrangement_position[j][0]
            cycle_size += 1
        if cycle_size > 0:
            number_of_swaps += cycle_size - 1
    return number_of_swaps


if __name__ == '__main__':
    print(minimum_swaps([1, 2, 3, 2, 1, 3]))
    print(minimum_swaps([1, 2, 3, 3, 1, 2]))