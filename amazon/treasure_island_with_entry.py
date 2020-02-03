"""
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure.
So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters.
You must start from one of the starting point (marked as S) of the map and can move one block up, down,
left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as
D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in.
Output the minimum number of steps to get to any of the treasure islands.
"""

import math


def find_treasure_util(grid, i, j):
    rows, columns = len(grid), len(grid[0])
    queue = [((i, j), 0)]
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[-1 for _ in range(columns)] for _ in range(rows)]
    while queue:
        (x, y), step = queue.pop()
        visited[x][y] = step
        for direction in directions:
            curr_x = x + direction[0]
            curr_y = y + direction[1]
            if 0 <= curr_x < rows and 0 <= curr_y < columns and grid[curr_x][curr_y] == 'X':
                return step + 1
            elif 0 <= curr_x < rows and 0 <= curr_y < columns \
                    and grid[curr_x][curr_y] != 'D' \
                    and visited[curr_x][curr_y] == -1:
                queue.append(((curr_x, curr_y), step + 1))
    return -1


def find_treasure(grid):
    if not len(grid) or not len(grid[0]):
        return -1
    minimum_steps = math.inf
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                minimum_steps = min(minimum_steps, find_treasure_util(grid, i, j))
    return minimum_steps


if __name__ == '__main__':
    grid = [['S', 'O', 'O', 'S', 'S'],
            ['D', 'O', 'D', 'O', 'D'],
            ['O', 'O', 'O', 'O', 'X'],
            ['X', 'D', 'D', 'O', 'O'],
            ['X', 'D', 'D', 'D', 'O']]
    print(find_treasure(grid))