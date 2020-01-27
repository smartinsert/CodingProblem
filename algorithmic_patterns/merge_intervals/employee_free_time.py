"""
For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
Our goal is to find out if there is a free interval that is common to all employees.
You can assume that each list of employee working hours is sorted on the start time.
"""
from heapq import *
from typing import List


# [[[1, 3], [5, 6]], [[2, 3], [6, 8]]]


def merge_intervals(intervals_a, intervals_b):
    intervals_a.extend(intervals_b)  # O(1)
    intervals_a.sort(key=lambda x: x[0])  # O(N*log(N))
    return intervals_a  # O(N*log(N))


def merge_overlapping_intervals(intervals):
    merged = []
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[1] <= end:
            end = max(interval[1], end)
        else:
            merged.append([start, end])
            start = interval[0]
            end = interval[1]
    merged.append([start, end])
    return merged


def free_time(merged_intervals):
    free_times = []
    for i in range(1, len(merged_intervals)):
        if merged_intervals[i][0] > merged_intervals[i - 1][1]:
            free_times.append([merged_intervals[i - 1][1], merged_intervals[i][0]])
    return free_times


# Solution using MinHeap

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'[{self.start}, {self.end}]'


class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index

    def __str__(self):
        return f'{str(self.interval)} {str(self.employee_index)} {str(self.interval_index)}'

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def employee_free_time(schedule: List[List[Interval]]):
    number_of_employees = len(schedule)
    free_times = []

    if not schedule or number_of_employees == 0:
        return free_times

    min_heap = []

    for employee in range(number_of_employees):
        heappush(min_heap, EmployeeInterval(schedule[employee][0], employee, 0))

    previous_interval = min_heap[0].interval

    while min_heap:
        next_employee_interval = heappop(min_heap)
        if previous_interval.end < next_employee_interval.interval.start:
            free_times.append(str(Interval(previous_interval.end, next_employee_interval.interval.start)))
        previous_interval = next_employee_interval.interval

        # If more intervals are available for the same employee, add their next interval
        employee_schedule = schedule[next_employee_interval.employee_index]
        if len(employee_schedule) > next_employee_interval.interval_index + 1:
            heappush(min_heap, EmployeeInterval(employee_schedule[next_employee_interval.interval_index + 1],
                                                next_employee_interval.employee_index,
                                                next_employee_interval.interval_index + 1
                                                )
                     )
    return free_times


if __name__ == '__main__':
    # print(free_time(merge_overlapping_intervals(merge_intervals([[1, 3], [5, 6]], [[2, 3], [6, 8]]))))
    # print(free_time(merge_overlapping_intervals(merge_intervals([[1, 3], [9, 12]], [[2, 4], [6, 8]]))))
    # print(free_time(merge_overlapping_intervals(merge_intervals([[1, 3], [2, 4]], [[3, 5], [7, 9]]))))

    print(employee_free_time([[Interval(1, 3), Interval(9, 12)], [Interval(2, 4), Interval(6, 8)]]))
