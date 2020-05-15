"""
Find the minimum number of edits to change one string to another
str1 = 'abc' str2 = 'yabc'
"""


def minimum_edit_distance(str1, str2):
    edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(len(str2) + 1):
        edits[i][0] = 1 + edits[i-1][0]

    for i in range(len(str2) + 1):
        for j in range(len(str1) + 1):
            if str2[i] == str1[j]:
                edits[i][j] = edits[i-1][j-1]
            else:
                edits[i][j] = 1 + min(edits[i-1][j], edits[i][j-1], edits[i-1][j-1])
    return edits[-1][-1]

