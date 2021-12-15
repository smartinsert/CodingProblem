"""
A ball is dropped into a special Galton board where at each level in the board the ball can only move right or down.
Given that the Galton board has M rows and N columns, return the total number of unique ways the ball can arrive at
the bottom right cell of the Galton board.

Ex: Given the following values of M and N…

M = 2, N = 2, return 2.
The possible paths are DOWN -> RIGHT and RIGHT -> DOWN
Ex: Given the following values of M and N…

M = 4, N = 3, return 10.
"""


def number_of_unique_ways(M: int, N: int):
    if not M and not N:
        return 0
    if M == 1 and N == 1:
        return 1
    stack = [(0, 0)]
    ways = 0

    while stack:
        x, y = stack.pop()
        if x == N - 1 and y == -(M - 1):
            ways += 1
        else:
            directions = [(x+1, y), (x, y-1)]
            for new_x, new_y in directions:
                if 0 <= x <= N - 1 and -(M - 1) <= y <= 0:
                    stack.append((new_x, new_y))
    return ways


def unique_ways_faster(M: int, N: int) -> int:
    if not M and not N:
        return 0
    if M == 1 and N == 1:
        return 1

    ways = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(M):
        for j in range(N):
            ways[i][0] = 1
            ways[0][j] = 1
    for i in range(1, M):
        for j in range(1, N):
            ways[i][j] = ways[i-1][j] + ways[i][j-1]
    return ways[-1][-1]


print(number_of_unique_ways(2, 2))
print(number_of_unique_ways(4, 3))
print(unique_ways_faster(4, 3))