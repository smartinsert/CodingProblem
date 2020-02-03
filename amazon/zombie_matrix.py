"""
Given a 2D grid (list of lists), each cell is either a zombie 1 or a human 0.
Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it
take to infect all humans?
"""


def min_hour(rows, columns, grid):
    times = 0
    Q = []
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                Q.append((i, j))

    while Q:
        for _ in range(len(Q)):
            x, y = Q.pop(0)
            for dir in directions:
                i = x + dir[0]
                j = y + dir[1]
                if 0 <= i < rows and 0 <= j < columns and grid[i][j] == 0:
                    grid[i][j] = 1
                    Q.append((i, j))
        times += 1
    return max(0, times - 1)


if __name__ == '__main__':
    matrix = [[0, 1, 1, 0, 1],
              [0, 1, 0, 1, 0],
              [0, 0, 0, 0, 1],
              [0, 1, 0, 0, 0]
              ]
    print(min_hour(4 ,4, matrix))