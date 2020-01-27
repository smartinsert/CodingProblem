"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. If there is no island return 0.
"""

from typing import List


def max_area_of_island(grid: List[List[int]]):
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(grid, i, j))
    return max_area


def dfs(grid, i, j):
    # Check boundary conditions
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] != 1:
        return 0
    grid[i][j] = 0
    count = 1
    count += dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j-1) + dfs(grid, i, j+1)
    return count

