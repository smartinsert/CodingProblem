"""
Find the max area trapped
"""


def find_the_max_area_of_water_trapped(heights):
    if not heights:
        return 0
    left_max, right_max = 0, 0
    water = [0 for _ in range(len(heights))]
    for i in range(len(heights)):
        height = heights[i]
        water[i] = left_max
        left_max = max(left_max, height)
    for i in reversed(range(len(heights))):
        height = heights[i]
        min_height = min(right_max, water[i])
        if height < min_height:
            water[i] = min_height - height
        else:
            water[i] = 0
        right_max = max(right_max, height)
    return sum(water)


