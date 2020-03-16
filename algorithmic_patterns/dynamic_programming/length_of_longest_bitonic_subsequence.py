"""
Find the length of longest bitonic subsequence
"""


def find_LBS(nums):
    n = len(nums)
    lds = [0 for _ in range(n)]
    lds_reverse = [0 for _ in range(n)]

    for i in range(n):
        lds[i] = 1
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i]:
                lds[i] = max(lds[i], 1 + lds[j])

    for i in range(n-1, -1, -1):
        lds_reverse[i] = 1
        for j in range(i+1, n):
            if nums[j] < nums[i]:
                lds_reverse[i] = max(lds_reverse[i], 1 + lds_reverse[j])

    max_length = 0
    for i in range(n):
        max_length = max(max_length, lds[i] + lds_reverse[i] - 1)
    return max_length