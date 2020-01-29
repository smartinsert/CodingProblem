import math
from typing import List


def container_with_most_water(heights: List[int]) -> int:
    if not heights:
        return 0
    max_area = -1 * math.inf
    i, j = 0, len(heights) - 1
    while i < j:
        min_height = min(heights[j], heights[i])
        max_area = max(max_area, min_height * (j - i))
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return max_area


if __name__ == '__main__':
    print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))