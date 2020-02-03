"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input:
11110
11010
11000
00000

Output: 1
"""


def number_of_islands(grid):
    if not grid:
        return 0
    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                num_islands += dfs(grid, i ,j)
    return num_islands


def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
        return 0
    grid[i][j] = '0'
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)
    return 1


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1','1','0','1', '0'],
            ['1','1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    print(number_of_islands(grid))



