"""
Find the longest common subsequence
"""


# Time: O(nm*min(m,n)); Space: O(nm*min(m,n))
def longest_common_subsequence(str1, str2):
    result = []
    if not str1 or not str2:
        return result

    lcs = [[[] for x in range(len(str1 + 1))] for y in range(len(str2 + 1))]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i-1] == str1[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + [str2[i-1]]
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j], key=len)
    return lcs[-1][-1]