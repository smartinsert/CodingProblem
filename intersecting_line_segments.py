"""
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0
and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments
connecting each point pi to qi.
Write an algorithm to determine how many pairs of the line segments intersect.
"""


def intersecting_segments(p: list, q: list):
    ordered_pairs = list(zip(p, q))
    count = 0
    for i in range(len(ordered_pairs)):
        for j in range(i):
            p1, p2 = ordered_pairs[i], ordered_pairs[j]
            if (p1[0] < p2[0] and p1[1] > p2[1]) or (p1[0] > p2[0] and p1[1] < p2[1]):
                count += 1
    return count


if __name__ == '__main__':
    assert intersecting_segments([1, 4, 5], [4, 2, 3]) == 2
