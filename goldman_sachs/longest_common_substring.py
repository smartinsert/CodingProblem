"""
Given two strings 'X' and 'Y', find the length of the longest common substring.
"""
import math

def longest_common_substring_length(x: str, y: str) -> int:
    lengths = [[0 for _ in range(len(x) + 1)] for _ in range(len(y) + 1)]
    for i in range(len(x) + 1):
        lengths[i][0] = 0
    for j in range(len(y) + 1):
        lengths[j][0] = 0
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            lengths[i][j] = math.inf
            lengths[i][j] = 1 + min(lengths[i-1][j], lengths[i-1][j-1], lengths[i][j-1])
    return lengths[len(x)][len(y)]


if __name__ == '__main__':
    print(longest_common_substring_length('abcae', 'abcef'))