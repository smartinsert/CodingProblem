"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""

from typing import List


def trapped_rain_water(heights: List[int]) -> int:
    length = len(heights)
    left = [0 for _ in range(length)]
    right = [0 for _ in range(length)]
    water_trapped = 0
    left[0] = heights[0]
    for i in range(1, length):
        left[i] = max(left[i-1], heights[i])
    right[length-1] = heights[length-1]
    for i in range(length-2, -1, -1):
        right[i] = max(right[i+1], heights[i])
    for i in range(length):
        water_trapped += min(left[i], right[i]) - heights[i]
    return water_trapped


if __name__ == '__main__':
    # print(trapped_rain_water([2, 0, 2]))
    # print(trapped_rain_water([3, 0, 0, 2, 0, 4]))
    print(trapped_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))