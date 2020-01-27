"""
Given two lists of intervals, find the intersection of these two lists.
Each list consists of disjoint intervals sorted on their start time.
"""


def interval_intersection(source_intervals, target_intervals):
    result = []
    i, j, start, end = 0, 0, 0, 1
    while i < len(source_intervals) and j < len(target_intervals):
        a_overlaps_b = target_intervals[j][start] <= source_intervals[i][start] <= target_intervals[j][end]
        b_overlaps_a = source_intervals[i][start] <= target_intervals[j][start] <= source_intervals[i][end]
        if a_overlaps_b or b_overlaps_a:
            result.append([max(source_intervals[i][start], target_intervals[j][start]),
                          min(source_intervals[i][end], source_intervals[j][end])])
        if source_intervals[i][end] < target_intervals[j][end]:
            i += 1
        else:
            j += 1
    return result


if __name__ == '__main__':
    print(interval_intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))