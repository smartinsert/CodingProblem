"""
. In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal
 to the ‘end’ of ‘i’.

Write a function to return an array containing indices of the next interval of each input interval. If there is no next
interval of a given interval, return -1. It is given that none of the intervals have the same start point.
"""

from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)


def find_next_interval(intervals):
    result = [0] * len(intervals)
    max_start_heap, max_end_heap = [], []
    for idx, interval in enumerate(intervals):
        heappush(max_end_heap, (-interval.end, idx))
        heappush(max_start_heap, (-interval.start, idx))

    while max_end_heap:
        top_end, end_index = heappop(max_end_heap)
        result[end_index] = -1
        if -max_start_heap[0][0] >= -top_end:
            top_start, start_idx = heappop(max_start_heap)
            while max_start_heap and -max_start_heap[0][0] >= -top_end:
                top_start, start_idx = heappop(max_start_heap)
            result[end_index] = start_idx
            heappush(max_start_heap, (top_start, start_idx))
    return result


def main():
    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
