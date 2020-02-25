"""
Given a number sequence, find the length of its Longest Increasing Subsequence (LIS).
In an increasing subsequence, all the elements are in increasing order (from lowest to highest).
"""


def longest_increasing_subsequence(arr):
    if len(arr) == 0:
        return 0
    return longest_increasing_subsequence_util(arr, 0, -1)


def longest_increasing_subsequence_util(arr, current_index, previous_index):
    if current_index == len(arr):
        return 0
    c1 = 0
    if previous_index == -1 or arr[current_index] > arr[previous_index]:
        c1 = 1 + longest_increasing_subsequence_util(arr, current_index + 1, current_index)
    c2 = longest_increasing_subsequence_util(arr, current_index + 1, previous_index)
    return max(c1, c2)


def longest_increasing_top_down(arr):
    if len(arr) == 0:
        return 0
    dp = [[-1 for _ in range(len(arr) + 1)] for _ in range(len(arr) + 1)]
    return longest_increasing_top_down_util(arr, dp, 0, -1)


def longest_increasing_top_down_util(arr, dp, current_index, previous_index):
    if current_index == len(arr):
        return 0

    c1 = 0
    if dp[current_index][previous_index + 1] == -1:
        if arr[current_index] > arr[previous_index] or previous_index == -1:
            c1 = 1 + longest_increasing_top_down_util(arr, dp, current_index + 1, current_index)
        c2 = longest_increasing_top_down_util(arr, dp, current_index + 1, previous_index)
        dp[current_index][previous_index + 1] = max(c1, c2)
    return dp[current_index][previous_index + 1]


def longest_increasing_bottom_up(arr):
    if len(arr) == 0:
        return 0
    dp = [0 for _ in range(len(arr))]
    return longest_increasing_bottom_up_util(arr, dp)


def longest_increasing_bottom_up_util(arr, dp):
    dp[0] = 1
    max_length = 1
    for i in range(1, len(arr)):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                max_length = max(max_length, dp[i])
    return max_length


if __name__ == '__main__':
    print(longest_increasing_subsequence([4, 2, 3, 6, 10, 1, 12]))
    print(longest_increasing_top_down([4, 2, 3, 6, 10, 1, 12]))
    print(longest_increasing_bottom_up([4, 2, 3, 6, 10, 1, 12]))