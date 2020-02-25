"""
Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.
Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
"""

from math import sqrt
from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return other.distance_from_origin() < self.distance_from_origin()

    def distance_from_origin(self):
        return sqrt((self.x * self.x) + (self.y * self.y))

    def __repr__(self):
        return f'({self.x}, {self.y})'


def k_closest_points(points, k):
    if not points:
        return []
    max_heap = []
    structured_points = []
    for point in points:
        structured_points.append(Point(point[0], point[1]))
    for i in range(k):
        heappush(max_heap, structured_points[i])
    for i in range(k, len(structured_points)):
        if structured_points[i].distance_from_origin() < max_heap[0].distance_from_origin():
            heappop(max_heap)
            heappush(max_heap, structured_points[i])
    return list(max_heap)


if __name__ == '__main__':
    print(k_closest_points([[1,2],[1,3]], 1))
    print(k_closest_points([[1, 3], [3, 4], [2, -1]], 2))