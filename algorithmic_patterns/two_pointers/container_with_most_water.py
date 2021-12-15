"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
"""


def container_with_most_water_naive(height: []) -> int:
    if len(height) < 2:
        return 0
    max_area = float('-inf')
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            min_height = min(height[i], height[j])
            max_area = max(max_area, min_height * (j - i))
    return max_area


def container_with_most_water(height: []) -> int:
    if len(height) < 2:
        return 0
    max_area = float('-inf')
    left, right = 0, len(height) - 1
    while left < right:
        min_height = min(height[left], height[right])
        max_area = max(max_area, min_height * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
