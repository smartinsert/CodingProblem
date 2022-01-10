"""
Given a 2D array containing only the following values: -1, 0, 1 where -1 represents an obstacle, 0 represents a rabbit hole,
and 1 represents a rabbit, update every cell containing a rabbit with the distance to its closest rabbit hole.

Note: multiple rabbit may occupy a single rabbit hole and you may assume every rabbit can reach a rabbit hole. A rabbit can only move up, down, left, or right in a single move. Ex: Given the following grid…

-1  0  1
 1  1 -1
 1  1  0
your grid should look like the following after running the function...
-1  0  1
2  1 -1
2  1  0

Ex: Given the following grid…

 1  1  1
 1 -1 -1
 1  1  0
your grid should look like the following after running the function...
4  5  6
3 -1 -1
2  1  0
"""

import sys


def compute_distance_to_rabbit_holes(grid: [[]]):
    if not grid:
        return grid

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                grid[i][j] = sys.maxsize

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                search(grid, i, j, 0)


def search(grid, row, col, distance):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] < distance:
        return
    grid[row][col] = distance
    search(grid, row - 1, col, distance + 1)
    search(grid, row, col - 1, distance + 1)
    search(grid, row + 1, col, distance + 1)
    search(grid, row, col + 1, distance + 1)


grid = [[-1, 0, 1],
        [1, 1, -1],
        [1, 1, 0]]

grid1 = [[1, 1, 1],
        [1, -1, -1],
        [1, 1, 0]]

compute_distance_to_rabbit_holes(grid)
compute_distance_to_rabbit_holes(grid1)

print(grid)
print(grid1)


