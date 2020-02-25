"""
Given N x M character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)
"""


def find_number_of_black_shapes(matrix, rows, columns):
    number = 0
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = []
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 'X':
                queue.append((i, j))

    while queue:
        for _ in range(len(queue)):
            cur_x, cur_y = queue.pop(0)
            for direction in directions:
                new_x = cur_x + direction[0]
                new_y = cur_y + direction[1]
                # Check boundary conditions
                if 0 <= new_x < rows and 0 <= new_y < columns and matrix[new_x][new_y] == '0':
                    matrix[new_x][new_y] = 'X'
                    queue.append((new_x, new_y))
        number += 1

    return max(0, number - 1)


if __name__ == '__main__':
    matrix = [["0", "0", "0", "X", "0", "0", "0"],
              ["0", "0", "X", "X", "0", "X", "0"],
              ["0", "X", "0", "0", "0", "X", "0"]
             ]
    print(find_number_of_black_shapes(matrix, len(matrix), len(matrix[0])))
