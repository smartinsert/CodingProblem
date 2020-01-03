from collections import Counter
from itertools import combinations


def sherlockAndAnagrams(s):
    count = []
    for i in range(1, len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        b = Counter(a)
        count.append(sum([len(list(combinations(['a']*b[j], 2))) for j in b]))
    return sum(count)


if __name__ == '__main__':
    print(sherlockAndAnagrams('ifailuhkqq'))
    print(sherlockAndAnagrams('kkkk'))