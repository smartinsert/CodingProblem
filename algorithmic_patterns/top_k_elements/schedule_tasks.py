"""
Schedule tasks on a cpu such that each task is k cycles apart
"""

from heapq import *


# Time: O(N*logN); Space:
def schedule_tasks(tasks, k):
    n = len(tasks)
    result = []
    if n == 0:
        return result

    task_to_frequency = {}
    interval_count = 0

    for character in tasks:
        if character not in task_to_frequency:
            task_to_frequency[character] = 0
        task_to_frequency[character] += 1

    max_heap = []

    # Insert all the tasks
    for task, frequency in task_to_frequency.items():
        heappush(max_heap, (-frequency, task))

    while max_heap:
        wait_list = []
        n = k + 1
        while n > 0 and max_heap:
            interval_count += 1
            frequency, task = heappop(max_heap)
            if -frequency > 1:
                wait_list.append((frequency + 1, task))
            n -= 1

        for frequency, task in wait_list:
            heappush(max_heap, (frequency, task))

        if max_heap:
            interval_count += n
    return interval_count


