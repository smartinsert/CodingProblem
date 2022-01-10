# Min cost Path

def min_cost_path(grid: [[]]) -> int:
    if not grid:
        return 0
    return dfs(grid, 0, 0)


def dfs(grid: [[]], row: int, col: int):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 100000

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return grid[row][col]

    right = grid[row][col] + dfs(grid, row, col + 1)
    down = grid[row][col] + dfs(grid, row + 1, col)

    return min(right, down)


def min_cost_path_dp(grid: [[]]):
    if not grid:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j > 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0 and i > 0:
                grid[i][j] += grid[i-1][j]
            elif i > 0 and j > 0:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


print(min_cost_path([
    [1, 1, 3],
    [2, 3, 1],
    [4, 6, 1]
]))


print(min_cost_path_dp([
    [1, 1, 3],
    [2, 3, 1],
    [4, 6, 1]
]))

