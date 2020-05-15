"""
Given a list of intervals representing the start and end time of ‘N’ meetings,
find the minimum number of rooms required to hold all the meetings.
"""
from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting end
        return self.end < other.end

    def __str__(self):
        return f'[{self.start}, {self.end}]'


# Time: O(NlogN); Space: O(N) for sorting
def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x.start)

    min_rooms = 0
    min_heap = []

    for meeting in meetings:
        # remove all meetings that have ended
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)
        # push the current meeting
        heappush(min_heap, meeting)
        min_rooms = max(min_rooms, len(min_heap))
    print(f'Active meetings {len(min_heap)}, {min_heap}')
    return min_rooms


if __name__ == '__main__':
    # print(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)]))
    # print(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)]))
    # print(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)]))
    print(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(10, 12), Meeting(5, 9), Meeting(5, 12)]))