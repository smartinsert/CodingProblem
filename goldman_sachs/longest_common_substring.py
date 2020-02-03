"""
Given two strings 'X' and 'Y', find the length of the longest common substring.
"""
import math


def longest_common_substring_length(x: str, y: str) -> int:
    result = -math.inf
    lengths = [[0 for _ in range(len(x) + 1)] for _ in range(len(y) + 1)]
    for i in range(len(x) + 1):
        lengths[i][0] = 0
    for j in range(len(y) + 1):
        lengths[j][0] = 0
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i-1] == y[j-1]:
                lengths[i][j] = lengths[i-1][j-1] + 1
                result = max(result, lengths[i][j])
            else:
                lengths[i][j] = 0
    return result


if __name__ == '__main__':
    print(longest_common_substring_length('abcae', 'abcef'))
    print(longest_common_substring_length('abcdxyz', 'xyzabcd'))