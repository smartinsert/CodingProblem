"""
There is a rectangle with left bottom as  (0, 0) and right up as (x, y).
There are N circles such that their centers are inside the rectangle.
Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without
touching any circle.
"""


def is_valid(x, y, rows, columns):
    return 0 <= x < rows and 0 <= y < columns


def is_possible(m, n, k, r, X, Y):
    grid = [[0 for _ in range(n)] for _ in range(m)]
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    # Set all the vertices in the circle as blocked
    for i in range(m):
        for j in range(n):
            for c in range(k):
                if ((X[c] - i) * (X[c] - i)) + ((Y[c] - j) + (Y[c] - j)) <= r*r:
                    grid[i][j] = -1

    if grid[m-1][0] == -1:
        return False

    queue = []

    queue.append((m-1, 0))
    grid[m-1][0] = 1

    while queue:
        x, y = queue.pop(0)
        for direction in directions:
            i = x + direction[0]
            j = y + direction[1]

            if is_valid(i, j, m, n) and grid[i][j] == 0:
                grid[i][j] = 1
                queue.append((i, j))
    return grid[0][n-1] == 1


if __name__ == '__main__':
    m1 = 5
    n1 = 5
    k1 = 2
    r1 = 1
    X1 = [1, 3]
    Y1 = [3, 3]
    print(is_possible(m1, n1, k1, r1, X1, Y1))