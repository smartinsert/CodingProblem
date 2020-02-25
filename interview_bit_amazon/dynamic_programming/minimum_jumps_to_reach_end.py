"""
Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from
that element, write a program to find the minimum number of jumps needed to reach the end of the array
(starting from the first element). If an element is 0, then we cannot move through that element.
"""


import math


def minimum_jumps_to_reach_end(jumps):
    if len(jumps) == 0:
        return 0
    return minimum_jumps_recursive(jumps, 0)


def minimum_jumps_recursive(jumps, current_index):
    n = len(jumps)
    # Base condition 1
    if current_index == n-1:
        return 0

    # Base condition 2
    if jumps[current_index] == 0:
        return math.inf

    total_jumps = math.inf
    start, end = current_index + 1, current_index + jumps[current_index]
    while start <= end and start < n:
        minimum_jumps = minimum_jumps_recursive(jumps, start)
        start += 1
        if minimum_jumps != math.inf:
            total_jumps = min(total_jumps, 1 + minimum_jumps)
    return total_jumps


def minimum_jumps_dp(jumps):
    n = len(jumps)
    if n == 0:
        return 0

    dp = [math.inf for _ in range(n)]

    dp[0] = 0

    for start in range(n-1):
        end = start + 1
        while end <= start + jumps[start] and end < n:
            dp[end] = min(dp[end], 1 + dp[start])
            end += 1
    return dp[n-1]


if __name__ == '__main__':
    print(minimum_jumps_to_reach_end([2, 1, 1, 1, 4]))
    print(minimum_jumps_dp([2, 1, 1, 1, 4]))
