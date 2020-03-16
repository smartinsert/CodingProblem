"""
Find the length of the longest palindromic subsequence
"""


def find_LPS(input_str):
    n = len(input_str)
    if n == 0:
        return 0
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for start_index in range(n-1, -1, -1):
        for end_index in range(start_index+1, n):
            if input_str[start_index] == input_str[end_index]:
                dp[start_index][end_index] = 2 + dp[start_index+1][end_index-1]
            else:
                # skip either the first or the last character
                dp[start_index][end_index] = max(dp[start_index+1][end_index],
                                                 dp[start_index][end_index-1])
    return dp[0][n-1]


if __name__ == '__main__':
    print(find_LPS('abdbca'))