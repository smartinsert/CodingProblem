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
    for idx, interval in enumerate(existing_intervals):
        if new_interval.start > interval.end:
            merged.append(str(interval))
        elif new_interval.start < interval.end:
            end = max(new_interval.end, interval.end)
            if new_interval.end > interval.start:
                start = min(new_interval.start, interval.start)
            else:
                start = interval.start
            interval_to_merge = Interval(start, end)
            merged.append(str(interval_to_merge))
            new_interval = interval_to_merge
    return merged


if __name__ == '__main__':
    print(insert_interval([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6)))
    print(insert_interval([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10)))