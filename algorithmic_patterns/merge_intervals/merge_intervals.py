"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']'


def merge(intervals):
    merged = []

    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged.append(str(Interval(start, end)))
            start = interval.start
            end = interval.end
    merged.append(str(Interval(start, end)))
    return merged


def do_intervals_overlap(intervals):
    if len(intervals) < 2:
        return True
    intervals.sort(key=lambda x: x.start)
    end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            return True
        else:
            end = interval.end
    return False


if __name__ == '__main__':
    print(merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))
    print(do_intervals_overlap([Interval(1, 4), Interval(5, 6), Interval(7, 9)]))
    print(do_intervals_overlap([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))