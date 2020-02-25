"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The cell itself does not count as an adjacent cell.
The same letter cell may be used more than once.
"""


def does_word_exist(matrix, word):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == word[0]:
                if is_present(i, j, matrix, word, rows, columns, 0, []):
                    return True
    return False


def is_present(i, j, matrix, word, rows, columns, current_idx, visited):
    if (i, j) in visited:
        return False
    if current_idx == len(word):
        return True
    elif i < 0 or i >= rows or j < 0 or j >= columns:
        return False
    elif matrix[i][j] == word[current_idx]:
        # Perform DFS
        return is_present(i + 1, j, matrix, word, rows, columns, current_idx + 1, visited + [(i, j)]) or \
               is_present(i - 1, j, matrix, word, rows, columns, current_idx + 1, visited + [(i, j)]) or \
               is_present(i, j + 1, matrix, word, rows, columns, current_idx + 1, visited + [(i, j)]) or \
               is_present(i, j - 1, matrix, word, rows, columns, current_idx + 1, visited + [(i, j)])


if __name__ == '__main__':
    matrix = [
              ["A", "B", "C", "E"],
              ["S", "F", "C", "S"],
              ["A", "D", "E", "E"]
            ]

    print(does_word_exist(matrix, "ABCCED"))


