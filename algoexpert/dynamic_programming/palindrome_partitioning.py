"""
Find the minimum number of cuts required to make all the strings a palindrome
"""

import math


# Time: O(n^3) and Space: O(n^2)
def minimum_number_of_cuts(string):
    n = len(string)
    if n == 0:
        return 0
    palindrome = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            palindrome[i][j] = is_palindrome(string[i:j+1])

    cuts = [math.inf for _ in range(n)]

    for i in range(n):
        if palindrome[0][i]:
            cuts[i] = 0
        cuts[i] = 1 + cuts[i-1]
        for j in range(1, i):
            if palindrome[j][i] and cuts[j-1] + 1 < cuts[i]:
                cuts[i] = 1 + cuts[j-1]
    return cuts[-1]


def is_palindrome(string):
    start, end = 0, len(string) - 1
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        else:
            return False
    return True