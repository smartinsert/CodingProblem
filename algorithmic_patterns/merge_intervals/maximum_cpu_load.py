"""
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.
"""
from heapq import *


class Job:
    def __init__(self, start, end, load):
        self.start = start
        self.end = end
        self.load = load

    def __lt__(self, other):
        return self.end < other.end


def maximum_cpu_load(jobs):
    if len(jobs) < 1:
        return 0
    elif len(jobs) == 1:
        return jobs[0].load

    # Sort by start time
    jobs.sort(key=lambda x: x.start)

    current_cpu_load, max_cpu_load, min_heap = 0, 0, []

    for job in jobs:
        while len(min_heap) > 0 and job.start >= min_heap[0].end:
            current_cpu_load -= min_heap[0].load
            heappop(min_heap)
        heappush(min_heap, job)
        current_cpu_load += job.load
        max_cpu_load = max(current_cpu_load, max_cpu_load)
    return max_cpu_load


if __name__ == '__main__':
    print("Maximum CPU load at any time: " + str(maximum_cpu_load([Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(maximum_cpu_load([Job(6, 7, 10), Job(2, 4, 11), Job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(maximum_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)])))