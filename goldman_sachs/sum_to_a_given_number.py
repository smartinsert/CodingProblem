"""
Count number of subarrays that sum to a given number
"""

from typing import List


def count_subarrays(arr: List[int], target: int) -> int:
    count = 0
    for i in range(len(arr)):
        current_sum = arr[i]
        j = i + 1
        while j <= len(arr):
            if current_sum == target:
                count += 1
                break
            if j == len(arr):
                break
            current_sum += arr[j]
            j += 1
    return count


def count_subarrays_better(arr: List[int], target: int) -> int:
    prev_sum = dict()

    res = 0

    # Sum of elements so far.
    curr_sum = 0

    for i in range(0, len(arr)):

        # Add current element to sum so far.
        curr_sum += arr[i]

        # If currsum is equal to desired sum,
        # then a new subarray is found. So
        # increase count of subarrays.
        if curr_sum == target:
            res += 1

        # currsum exceeds given sum by currsum  - sum.
        # Find number of subarrays having
        # this sum and exclude those subarrays
        # from currsum by increasing count by
        # same amount.
        if (curr_sum - target) in prev_sum:
            res += prev_sum[curr_sum - target]

        # Add currsum value to count of
        # different values of sum.
        if curr_sum not in prev_sum:
            prev_sum[curr_sum] = 0
        prev_sum[curr_sum] += 1

    return res


if __name__ == '__main__':
    print(count_subarrays([10, 2, -2, -20, 10], -10))
    print(count_subarrays_better([10, 2, -2, -20, 10], -10))