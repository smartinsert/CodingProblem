"""
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a
shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left
corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a
block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D.
You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in.
The top-left corner is always safe. Output the minimum number of steps to get to the treasure.
"""
import math


def number_of_steps_to_find_treasure(grid):
    if not grid:
        return 0
    minimum_steps = math.inf
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                minimum_steps = min(minimum_steps, dfs(grid, i, j))
    return minimum_steps


def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 'D':
        return 0
    count = 1
    if grid[i][j] == 'O':
        grid[i][j] = 'D'
    elif grid[i][j] == 'X':
        count += 1
        return count
    return count + dfs(grid, i-1, j) + dfs(grid, i + 1, j) + dfs(grid, i, j - 1) + dfs(grid, i, j + 1)


def find_treasure(grid):
    if not len(grid) and not len(grid[0]):
        return -1
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    rows, columns = len(grid), len(grid[0])
    queue = [((0, 0), 0)]
    grid[0][0] = 'D'
    while queue:
        (x, y), step = queue.pop()
        for direction in directions:
            i = x + direction[0]
            j = y + direction[1]
            if 0 <= i < rows and 0 <= j < columns and grid[i][j] == 'X':
                return step + 1
            elif 0 <= i < rows and 0 <= j < columns and grid[i][j] == 'O':
                grid[i][j] = 'D'
                queue.append(((i, j), step + 1))
    return -1


if __name__ == '__main__':
    grid = [['O', 'O', 'O', 'O'],
            ['D', 'O', 'D', 'O'],
            ['O', 'O', 'O', 'O'],
            ['X', 'D', 'D', 'O']]
    print(find_treasure(grid))