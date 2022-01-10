"""
Given N points on a Cartesian plane, return the minimum time required to visit all points in the order that they’re
given.
Note: You start at the first point and can move one unit vertically, horizontally, or diagonally in a single second.

Ex: Given the following points…

points = [[0, 0], [1,1], [2,2]], return 2.
In one second we can travel from [0, 0] to [1, 1]
In another second we can travel from [1, 1,] to [2, 2]
Ex: Given the following points…

points = [[0, 1], [2, 3], [4, 0]], return 5.
"""


def time_to_travel(points: [[]]):
    if not points:
        return 0
    min_time = 0
    for idx in range(len(points) - 1):
        x_diff = abs(points[idx + 1][0] - points[idx][0])
        y_diff = abs(points[idx + 1][1] - points[idx][1])
        max_x_y = max(x_diff, y_diff)
        min_time += max_x_y
    return min_time


print(time_to_travel([[0, 0], [1, 1], [2, 2]]))
print(time_to_travel([[0, 1], [2, 3], [4, 0]]))

