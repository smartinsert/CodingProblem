"""
Given an array compute the prefix and suffix sum such that each index has the max value upto that index.
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2 ,1, 2, 1]
"""


def prefix_sum(arr: []) -> []:
    if len(arr) < 2:
        return arr
    max_val = float('-inf')
    result = [0] * len(arr)
    for i in range(len(arr)):
        max_val = max(max_val, arr[i])
        result[i] = max_val
    return result


def suffix_sum(arr: []) -> []:
    if len(arr) < 2:
        return arr
    max_val = float('-inf')
    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        max_val = max(max_val, arr[i])
        result[i] = max_val
    return result


def max_rain_water_trapped_better(arr: []) -> int:
    if len(arr) < 2:
        return 0
    water_level = 0
    prefix, suffix = prefix_sum(arr), suffix_sum(arr)
    for i in range(len(arr)):
        water_level += min(prefix[i], suffix[i]) - arr[i]
    return water_level


def max_rain_water_trapped_best(arr: []) -> int:
    if len(arr) < 2:
        return 0
    water_level, left, right, left_max, right_max = 0, 0, len(arr) - 1, float('-inf'), float('-inf')
    while left <= right:
        left_max, right_max = max(left_max, arr[left]), max(right_max, arr[right])
        if arr[left] <= arr[right]:
            water_level += left_max - arr[left]
            left += 1
        else:
            water_level += right_max - arr[right]
            right -= 1
    return water_level


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# print(prefix_sum(arr))
# print(suffix_sum(arr))
print(max_rain_water_trapped_better(arr))
print(max_rain_water_trapped_best(arr))
