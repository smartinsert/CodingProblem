"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
"""


def ways_to_decode(s):
    n = len(s)

    if n == 0:
        return 0
    elif n == 1:
        return 1 if is_upper_char(s[0]) else 0

    dp = [0 for _ in range(n + 1)]

    dp[0] = 1 if is_upper_char(s[0]) else 0
    dp[1] = dp[0] if is_upper_char(s[1]) else 0

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] if is_upper_char(s[i - 2:i]) else dp[i - 1]

    return dp[-1]


def is_upper_char(s):
    return chr(int(s) + 64).isupper()


if __name__ == '__main__':
    print(ways_to_decode('12'))

