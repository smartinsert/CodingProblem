"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map,
return the volume of water it can trap after raining.


Input: heightMap =
[
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
"""

import heapq


def total_water_trapped(grid: [[]]) -> int:
    if not grid:
        return 0
    seen = set()
    heap = []
    max_height, volume = -1, 0
    enqueue_boundaries(grid, heap, seen)

    while heap:
        height, i, j = heapq.heappop(heap)

        if height < max_height:
            volume += max_height - height
        else:
            max_height = height

        neighbours = [(i + 1, j), (i, j + 1), (i, j - 1), (i - 1, j)]

        for x, y in neighbours:
            enqueue_elements(grid, heap, x, y, seen)
    return volume


def enqueue_boundaries(grid: [[]], heap: [], seen: set) -> None:
    enqueue_top_and_bottom(grid, heap, seen)
    enqueue_left_and_right(grid, heap, seen)


def enqueue_top_and_bottom(grid: [[]], heap: [], seen: set) -> None:
    bottom_row_idx = len(grid) - 1

    for idx in range(len(grid[0])):
        enqueue_elements(grid, heap, 0, idx, seen)
        enqueue_elements(grid, heap, bottom_row_idx, idx, seen)


def enqueue_left_and_right(grid: [[]], heap: [], seen: set) -> None:
    last_column_index = len(grid[0]) - 1

    for idx in range(len(grid)):
        enqueue_elements(grid, heap, idx, 0, seen)
        enqueue_elements(grid, heap, idx, last_column_index, seen)


def enqueue_elements(grid: [[]], heap: [], i: int, j: int, seen: set) -> None:
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in seen:
        heapq.heappush(heap, (grid[i][j], i, j))
        seen.add((i, j))


print(total_water_trapped([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
print(total_water_trapped([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]))
