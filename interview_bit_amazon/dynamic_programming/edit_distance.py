"""
Given two strings A and B, find the minimum number of steps required to convert A to B.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Input 1:
    A = "abad"
    B = "abac"

Output 1:
    1

Explanation 1:
    Operation 1: Replace d with c.
"""


def edit_distance(A, B):
    return edit_distance_recursive(A, B, len(A) - 1, len(B) - 1)


def edit_distance_recursive(A, B, m, n):
    """
    We will perform all the operations on string A. For every character there are two options,
    1. If the two characters match, recur for the remaining strings
    2. Else get the minimum of either add, delete or update on first string
    :param A:
    :param B:
    :param m: length of string A
    :param n: length of string B
    :return: minimum edit distance
    """
    # If first string is empty, we need to insert all characters to match it with second
    if m == 0:
        return n

    # If second string is empty, we need to delete all characters to match it with second
    if n == 0:
        return m

    if A[m-1] == B[n-1]:
        return edit_distance_recursive(A, B, m-1, n-1)

    # recurse for the three cases and return minimum for add, replace, and update
    return 1 + min(
        edit_distance_recursive(A, B, m, n-1), # Insert
        edit_distance_recursive(A, B, m-1, n), # Delete
        edit_distance_recursive(A, B, m-1, n-1) # Replace
    )


def edit_distance_dp(A, B):
    m, n = len(A), len(B)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j-1],
                    dp[i-1][j],
                    dp[i-1][j-1]
                )
    return dp[m][n]


if __name__ == '__main__':
    print(edit_distance_recursive('abac', 'abad', 4, 4))
    print(edit_distance_dp('abac', 'abad'))