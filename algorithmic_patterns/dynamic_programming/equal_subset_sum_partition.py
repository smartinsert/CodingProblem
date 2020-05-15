"""
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in
both the subsets is equal.
"""


def equal_subset_sum(array):
    total_sum = sum(array)
    if total_sum % 2 != 0:
        return False
    return equal_subset_sum_recursive(array, total_sum // 2, 0)


def equal_subset_sum_recursive(array, required_sum, current_index):
    if current_index >= len(array) or len(array) == 0:
        return False

    if required_sum == 0:
        return True

    if array[current_index] <= required_sum and \
            equal_subset_sum_recursive(array, required_sum - array[current_index], current_index + 1):
        return True
    return equal_subset_sum_recursive(array, required_sum, current_index + 1)


def equal_subset_memoization(array):
    total_sum = sum(array)
    if total_sum % 2 != 0:
        return False
    dp = [[-1 for _ in range(sum(array) // 2 + 1)] for _ in range(len(array))]
    return True if equal_subset_memoization_recursion(array, total_sum // 2, 0, dp) == 1 else False


def equal_subset_memoization_recursion(array, required_sum, current_index, dp):
    n = len(array)
    if n == 0 or current_index >= n:
        return 0

    if required_sum == 0:
        return 1

    if dp[current_index][required_sum] != -1:
        return dp[current_index][required_sum]

    if array[current_index] <= required_sum and \
        equal_subset_memoization_recursion(array, required_sum - array[current_index], current_index + 1, dp):
        dp[current_index] = 1
        return 1
    return equal_subset_memoization_recursion(array, required_sum, current_index + 1, dp)


def equal_subset_sum_dp(array):
    required_sum = sum(array)
    if required_sum % 2 == 0:
        return False
    dp = [[False for _ in range(required_sum + 1)] for _ in range(len(array))]

    for i in range(len(array)):
        dp[i][0] = True

    for i in range(1, required_sum + 1):
        dp[0][i] = array[0] == i

    for i in range(1, len(array)):
        for j in range(required_sum + 1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= array[i]:
                dp[i][j] = dp[i-1][j - array[i]]
    return dp[len(array) - 1][required_sum]


