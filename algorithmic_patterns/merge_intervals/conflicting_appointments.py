"""
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.
"""


def conflicting_appointments(intervals):
    i, start, end = 1, 0, 1

    while i < len(intervals):
        interval_a = intervals[i-1]
        interval_b = intervals[i]
        a_overlaps_b = interval_b[start] <= interval_a[start] <= interval_b[end]
        b_overlaps_a = interval_a[start] <= interval_b[start] <= interval_a[end]
        if a_overlaps_b or b_overlaps_a:
            return False
        i += 1
    return True


def find_conflicting_appointments(intervals):
    start_idx, end_idx = 0, 1
    result = []
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][start_idx]
    end = intervals[0][end_idx]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[start_idx] < end:
            result.append([start, end])
            result.append(interval)
            end = max(interval[end_idx], end)
        else:
            start = interval[start_idx]
            end = interval[end_idx]
    return result


if __name__ == '__main__':
    # print(conflicting_appointments([[1,4], [2,5], [7,9]]))
    # print(conflicting_appointments([[6,7], [2,4], [8,12]]))

    print(find_conflicting_appointments([[4,5], [2,3], [3,6], [5,7], [7,8]]))