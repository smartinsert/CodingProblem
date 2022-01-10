"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""


def unique_paths(m: int, n: int):
    if not m and not n:
        return 0
    all_unique_paths = set()
    current_path = []
    dfs(m, n, 0, 0, current_path, all_unique_paths)
    return len(all_unique_paths)


def dfs(m, n, i, j, current_path, all_unique_paths):
    if i >= m or j >= n:
        return

    current_path.append((i, j))

    if i == m - 1 and j == n - 1:
        all_unique_paths.add(tuple(current_path))

    else:
        dfs(m, n, i+1, j, current_path, all_unique_paths)
        dfs(m, n, i, j+1, current_path, all_unique_paths)

    current_path.pop()


print(unique_paths(3, 7))
print(unique_paths(3, 2))
