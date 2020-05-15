"""
Count the river sizes in a matrix
"""


def river_sizes(matrix):
    if len(matrix) == 0:
        return []
    result = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                result.append(dfs(matrix, i, j))
    return result


def dfs(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]) or matrix[i][j] != 1:
        return 0
    matrix[i][j] = 0
    count = 1
    count += dfs(matrix, i-1, j) + dfs(matrix, i+1, j) + dfs(matrix, i, j-1) + dfs(matrix, i, j-1)
    return count


if __name__ == '__main__':
    matrix = [[1, 0, 0, 1, 0],
              [1, 0, 1, 0, 0],
              [0, 0, 1, 0, 1],
              [1, 0, 1, 0, 1],
              [1, 0, 1, 1, 0]
              ]
    print(river_sizes(matrix))
