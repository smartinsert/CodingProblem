"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
the sum of all numbers along its path.
"""


def minimum_path_sum(cost, m, n):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    dp[0][0] = cost[0][0]

    for i in range(1, m+1):
        dp[0][i] = dp[0][i-1] + cost[0][i]

    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] + cost[i][0]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[n][m]


if __name__ == '__main__':
    mat = [[1, 2, 3],
           [4, 8, 2],
           [1, 5, 3],
           [6, 2, 9]]
    print(minimum_path_sum(mat, 2, 3))