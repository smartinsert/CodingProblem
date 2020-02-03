"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


def search_matrix(matrix, target):
    if not len(matrix) or not len(matrix[0]):
        return False
    high = len(matrix[0]) - 1
    low = 0

    while low < len(matrix) and high >= 0:
        if matrix[high][low] > target:
            high -= 1
        elif matrix[high][low] < target:
            low += 1
        elif matrix[high][low] == target:
            return True
    return False


if __name__ == '__main__':
    matrix = [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
             ]

    print(search_matrix(matrix, 5))



