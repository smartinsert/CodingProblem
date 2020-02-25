"""
Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.

Input 2:
    A = "aab"

Output 2:
    1

Explanation 2:
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


def is_a_palindrome(string, low, high):
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


def palindrome_partitioning(string):
    return minimum_cuts_required(string, 0, len(string) - 1)


def minimum_cuts_required(string, start, end):
    if start >= end or is_a_palindrome(string, start, end):
        return 0
    # at max we need to make cuts at each point in the string
    minimum_cuts = end - start
    for i in range(start, end + 1):
        if is_a_palindrome(string, start, i):
            # We can cut here and recurse for the rest of the string
            minimum_cuts = min(minimum_cuts, 1 + minimum_cuts_required(string, i+1, end))
    return minimum_cuts


def palindrome_partitioning_bottom_up(string):
    n = len(string)

    if n == 0:
        return 0

    is_palindrome = [[False for _ in range(n)] for _ in range(n)]

    # All unit length strings are palindrome
    for i in range(n):
        is_palindrome[i][i] = True

    # Fill the palindrome table
    for start in range(n-1, -1, -1):
        for end in range(start + 1, n):
            if string[start] == string[end]:
                if end - start == 1 or is_palindrome[start + 1][end - 1]:
                    is_palindrome[start][end] = True

    # Build table for cuts
    cuts = [0 for _ in range(n)]

    for start in range(n-1, -1, -1):
        minimum_cuts = n
        for end in range(n-1, start - 1, -1):
            if is_palindrome[start][end]:
                minimum_cuts = 0 if end == n - 1 else min(minimum_cuts, 1 + cuts[end + 1])
        cuts[start] = minimum_cuts
    return cuts[0]


def palindrome_partitioning_better(string):
    n = len(string)
    if n == 0:
        return 0

    is_palindrome = [[False for _ in range(n)] for _ in range(n)]
    cuts = [0 for _ in range(n)]

    for i in range(1, n):
        minimum_cuts = i
        for j in range(i+1):
            # Check palindrome
            if string[i] == string[j] and ((i - j) <= 1 or is_palindrome[i-1][j+1]):
                is_palindrome[i][j] = True
                minimum_cuts = min(minimum_cuts, 0 if j == 0 else 1 + cuts[j-1])
        cuts[i] = minimum_cuts
    return cuts[n-1]



if __name__ == '__main__':
    # print(palindrome_partitioning('aba'))
    # print(palindrome_partitioning('aab'))
    # print(palindrome_partitioning('ababb'))
    # print(palindrome_partitioning('cddpd'))
    print(palindrome_partitioning_bottom_up('cddpd'))
    print(palindrome_partitioning_better('cddpd'))