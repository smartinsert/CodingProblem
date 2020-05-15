"""
Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower
right).

An N-by-N square matrix is a Latin square if each cell contains one of N different values, and no value is repeated
within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the
integers between 1 and N.

Given a matrix that contains only integers between 1 and N, we want to compute its trace and check whether it is a
natural Latin square. To give some additional information, instead of simply telling us whether the matrix is a natural
Latin square or not, please compute the number of rows and the number of columns that contain repeated values.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each starts with a line containing
a single integer N: the size of the matrix to explore. Then, N lines follow. The i-th of these lines contains N integers
 Mi,1, Mi,2 ..., Mi,N. Mi,j is the integer in the i-th row and j-th column of the matrix.

Output
For each test case, output one line containing Case #x: k r c, where x is the test case number (starting from 1), k is
the trace of the matrix, r is the number of rows of the matrix that contain repeated elements, and c is the number of
columns of the matrix that contain repeated elements.
"""


def is_a_latin_square(matrix, case):

    rows = len(matrix)
    columns = len(matrix[0])

    result = 'Case #{x}: {k} {r} {c}'
    if rows == 0 and columns == 0:
        return result.format(-1, 0, 0, 0)
    trace = sum(matrix[idx][idx] for idx in range(rows))
    seen = set()
    duplicate_rows, duplicate_columns = set(), set()
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] not in seen:
                seen.add(matrix[i][j])
            else:
                duplicate_rows.add(i)
        seen = set()

    for i in range(columns):
        for j in range(rows):
            if matrix[j][i] not in seen:
                seen.add(matrix[j][i])
            else:
                duplicate_columns.add(i)
        seen = set()
    return result.format(x=case, k=trace, r=len(duplicate_rows), c=len(duplicate_columns))


if __name__ == '__main__':
    number_of_test_cases = int(input())
    for case in range(number_of_test_cases):
        size_of_matrix = int(input())
        matrix = []
        for i in range(size_of_matrix):
            row = list(map(int, input().rstrip().split()))
            matrix.append(row)
        print(is_a_latin_square(matrix, case + 1))


