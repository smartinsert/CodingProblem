"""
Given a list of non-overlapping intervals sorted by their start time,
insert a given interval at the correct position and merge all necessary intervals to produce a list that has
only mutually exclusive intervals.
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'


def insert_interval(existing_intervals, new_interval):
    # We have sorted non-overlapping intervals
    merged = []
    i = 0
    while i < len(existing_intervals) and existing_intervals[i].end < new_interval.start:
        merged.append(str(existing_intervals[i]))
        i += 1

    # if the existing interval overlaps with the new interval
    while i < len(existing_intervals) and existing_intervals[i].start <= new_interval.end:
        new_interval.start = min(existing_intervals[i].start, new_interval.start)
        new_interval.end = max(existing_intervals[i].end, new_interval.end)
        i += 1
    merged.append(str(new_interval))
    while i < len(existing_intervals):
        merged.append(str(existing_intervals[i]))
        i += 1
    return merged


if __name__ == '__main__':
    print(insert_interval([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6)))
    print(insert_interval([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10)))