"""
Given a matrix containing 0's and 1's find the largest square matrix with all 1's
"""


def find_largest_square_size(matrix):
    rows, columns = len(matrix), len(matrix[0])
    if rows == 0 or columns == 0:
        return 0
    dp = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]

    max_square = 0

    for i in range(rows):
        dp[i][0] = matrix[i][0]
        if dp[i][0] == 1:
            max_square = 1

    for j in range(columns):
        dp[0][j] = matrix[0][j]
        if dp[0][j] == 1:
            max_square = 1

    for i in range(1, rows+1):
        for j in range(1, columns+1):
            if matrix[i-1][j-1] == 0:
                continue
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                if dp[i][j] > max_square:
                    max_square = dp[i][j]
    return max_square


if __name__ == '__main__':
    matrix = [[0, 0, 1, 0, 1, 1],
              [0, 1, 1, 1, 0, 0],
              [0, 0, 1, 1, 1, 1],
              [1, 1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1, 1],
              [1, 1, 0, 1, 1, 1],
              [1, 0, 1, 1, 1, 1],
              [1, 1, 1, 0, 1, 1]
              ]

    print(find_largest_square_size(matrix))