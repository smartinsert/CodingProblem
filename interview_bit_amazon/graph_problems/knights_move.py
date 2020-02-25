"""
Given a square chessboard of N x N size, the position of Knight and position of a target is given.
We need to find out minimum steps a Knight will take to reach the target position.
"""


class Cell:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance


def is_valid(x, y, grid_size):
    return 0 <= x < grid_size and 0 <= y <= grid_size


def minimum_steps_to_reach_destination(grid_size, start, end):
    x = [2, 2, 1, 1, 1, -1, 2, -2]
    y = [1, -1, 2, -2, 2, 2, 1, 1]
    directions = list(zip(x, y))
    visited = [[False for _ in range(grid_size + 1)] for _ in range(grid_size + 1)]

    queue = []

    queue.append(Cell(start[0], start[1], 0))

    visited[start[0]][start[1]] = True

    while queue:
        current_cell = queue.pop(0)

        if current_cell.x == end[0] and current_cell.y == end[1]:
            return current_cell.distance

        for direction in directions:
            x = current_cell.x + direction[0]
            y = current_cell.y + direction[1]

            if is_valid(x, y, grid_size) and not visited[x][y]:
                visited[x][y] = True
                queue.append((Cell(x, y, current_cell.distance + 1)))


if __name__ == '__main__':
    print(minimum_steps_to_reach_destination(30, [1, 1], [30, 30]))