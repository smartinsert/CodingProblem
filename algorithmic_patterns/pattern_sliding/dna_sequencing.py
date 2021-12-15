from typing import List


def findRepeatedDnaSequences(s: str) -> List[str]:
    if not s:
        return []
    seq = s[0:10]  # starting with first 10-length sequence
    listt = []
    dictt = {}
    # we are going to keep the count of every possible 10-length sequence in this dict
    for i in range(10, len(s) + 1):
        if seq not in dictt:
            dictt[seq] = 1
        else:
            dictt[seq] += 1
        if i != len(s):
            seq = seq[1:] + str(s[i])  # sliding window
    for x in dictt.keys():
        if dictt[x] > 1:
            listt.append(x)  # appending only those sequences which are occuring more than once
    return listt


print(findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
