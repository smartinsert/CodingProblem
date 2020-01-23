"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close
to the target number as possible, return the sum of the triplet. If there are more than one such triplet,
return the sum of the triplet with the smallest sum.
"""


def triplet_sum_close_to_target(arr: list, target: int) -> int:
    arr.sort()
    smallest_difference = float('inf')
    for i in range(len(arr)):
        smallest_difference = search_pair(arr, target, arr[i], i + 1, smallest_difference)
    return smallest_difference


def search_pair(arr, target_sum, current_number, left, smallest_difference):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        target_diff = target_sum - current_number - current_sum
        if target_diff == 0:
            return target_diff - target_sum
        if abs(target_diff) < abs(smallest_difference) or \
                (abs(target_diff) == abs(smallest_difference) and target_diff >= smallest_difference):
            smallest_difference = target_diff
        if target_diff > 0:
            left += 1
        else:
            right -= 1
    return smallest_difference


if __name__ == '__main__':
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))