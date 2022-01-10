"""
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0
Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0
"""
import heapq
from heapq import *


def find_sliding_window_median_heap(nums, k):
    min_heap, max_heap, result = [], [], []
    for idx, number in enumerate(nums):
        if not max_heap or number <= -max_heap[0]:
            heappush(max_heap, -number)
        else:
            heappush(min_heap, number)
        rebalance_heaps(min_heap, max_heap)

        if idx - k + 1 >= 0:
            if len(max_heap) == len(min_heap):
                median = (-max_heap[0] + min_heap[0]) / 2
                result.append(median)
            else:
                result.append(-max_heap[0])
            element_to_remove = nums[idx-k+1]
            if element_to_remove <= -max_heap[0]:
                remove(max_heap, -element_to_remove)
            else:
                remove(min_heap, element_to_remove)
            rebalance_heaps(min_heap, max_heap)
    return result


def remove(heap: [], element: int):
    idx = heap.index(element)
    heap[idx] = heap[-1]
    del heap[-1]

    if idx < len(heap):
        heapq._siftup(heap, idx)
        heapq._siftdown(heap, 0, idx)


def rebalance_heaps(min_heap, max_heap):
    if len(max_heap) > len(min_heap) + 1:
        heappush(min_heap, -heappop(max_heap))
    elif len(max_heap) < len(min_heap):
        heappush(max_heap, -heappop(min_heap))




def find_sliding_window_median(nums, k):
    result = []
    current_window = []
    window_start = 0
    for window_end in range(len(nums)):
        current_window.append(nums[window_end])
        if window_end - window_start + 1 >= k:
            window_length = len(current_window)
            mid = window_length // 2
            if len(current_window) % 2 == 0:
                median = (current_window[mid - 1] + current_window[mid]) / 2
            else:
                sorted_nums = sorted(current_window)
                median = sorted_nums[mid]
            result.append(median)
            current_window.pop(0)
            window_start += 1
    # TODO: Write your code here
    return result


def main():
    result = find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    result = find_sliding_window_median_heap(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
