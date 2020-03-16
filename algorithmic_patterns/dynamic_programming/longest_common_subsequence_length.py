"""
Find the length of the longest common subsequence
"""


def longest_common_subsequence(str1, str2):
    n, m = len(str1), len(str2)
    if n == 0:
        return 0
    if m == 0:
        return 0
    # assume n > m
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(0, m+1):
        dp[i][0] = 0
        for j in range(0, n+1):
            dp[0][j] = 0
            if str2[i-1] == str1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


if __name__ == '__main__':
    print(longest_common_subsequence('abcdaf', 'acbcf'))
    print(longest_common_subsequence('ABCDGHLQR', 'AEDPHR'))