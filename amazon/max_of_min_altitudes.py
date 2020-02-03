"""
Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1].
The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.
Don't include the first or final entry. You can only move either down or right at any point in time.
"""

from heapq import *
import math


def max_of_min_altitudes_util(grid, i, j):
    rows = len(grid)
    columns = len(grid[0])
    visited = [[-1 for _ in range(columns)] for _ in range(rows)]
    directions = [[0, 1], [1, 0]]
    queue = [(i, j)]
    path_heap = []
    while queue:
        x, y = queue.pop()
        visited[x][y] += 1
        value = grid[i][j]
        heappush(path_heap, value)
        for direction in directions:
            i = x + direction[0]
            j = y + direction[1]
            if 0 <= i < rows-1 and 0 <= j < columns-1:
                value = grid[i][j]
                heappush(path_heap, value)
            if 0 <= i < rows and 0 <= j < columns and visited[x][y] == -1:
                queue.append((i, j))
    return heappop(path_heap)


def max_of_min_altitude(grid):
    if not len(grid) or not len(grid[0]):
        return -1
    max_value = -math.inf
    directions = [[1, 0], [0, 1]]
    start = (0, 0)
    for direction in directions:
        max_value = max(max_of_min_altitudes_util(grid, start[0] + direction[0], start[1] + direction[1]), max_value)
    return max_value


if __name__ == '__main__':
    grid = [[5, 1],
            [4, 5]]
    grid_1 = [[1, 2, 3],
              [4, 5, 1]]
    print(max_of_min_altitude(grid))
    print(max_of_min_altitude(grid_1))