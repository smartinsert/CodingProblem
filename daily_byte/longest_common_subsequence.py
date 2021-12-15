"""
Given two strings, s and t, return the length of their longest subsequence.

Ex: Given the following strings s and t…

s = "xyz", t = "xyz". return 3.
Ex: Given the following strings s and t…

s = "abca", t = "acea", return 3.
Ex: Given the following strings s and t…

s = "abc", t = "def", return 0.
"""


def longest_common_subsequence(s: str, t: str) -> int:
    if not s or not t:
        return 0
    return length_of_lcs(s, t)


def length_of_lcs(s: str, t: str) -> int:
    if not s or not t:
        return 0
    if s[-1] == t[-1]:
        return 1 + length_of_lcs(s[:-1], t[:-1])
    else:
        return max(length_of_lcs(s[:-1], t), length_of_lcs(s, t[:-1]))


print(longest_common_subsequence('xyz', 'xyz'))
print(longest_common_subsequence('abca', 'acea'))
print(longest_common_subsequence('abc', 'def'))

