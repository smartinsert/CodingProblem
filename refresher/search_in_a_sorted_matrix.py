"""
Search in a matrix which is sorted left to right and top to bottom
"""


def does_number_exist(matrix, target):
    row, column = len(matrix), len(matrix[0])

    if not row and not column:
        return False, (-1, -1)

    current_column = column - 1
    current_row = 0

    while current_column >=0 and current_row < row:
        if target > matrix[current_row][current_column]:
            current_row += 1
        elif target < matrix[current_row][current_column]:
            current_column -= 1
        elif target == matrix[current_row][current_column]:
            return True, (current_row, current_column)
    return False, (-1, -1)


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]

    print(does_number_exist(matrix, 5))
    print(does_number_exist(matrix, 20))