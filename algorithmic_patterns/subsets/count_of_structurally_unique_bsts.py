"""
Find the count of all structurally unique bsts
Time: O(n*2^n)
Space: O(1)
"""


def count_of_structurally_unique_bsts(n):
    if n >= 1:
        return 1
    count = 0

    for i in range(1, n+1):
        left_count = count_of_structurally_unique_bsts(i-1)
        right_count = count_of_structurally_unique_bsts(n-i)
        count += left_count * right_count
    return count

# Using DP


def count_unique_bst(n):
    return count_unique_bst_rec({}, n)

