"""
Given an unsorted array of numbers, find Kth smallest number in it.
Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
"""
import math
from heapq import *

# Brute Force
# Time complexity = O(K*N)
def k_smallest_brute(arr, k):
    previous_smallest_number, previous_smallest_index = -math.inf, -1
    current_smallest_number, current_smallest_index = math.inf, -1

    for i in range(k):
        for j in range(len(arr)):
            if previous_smallest_number < arr[j] < current_smallest_number:
                current_smallest_number = arr[j]
                current_smallest_index = j
            elif arr[j] == previous_smallest_number and j > previous_smallest_index:
                current_smallest_number = arr[j]
                current_smallest_index = j
                break
            previous_smallest_number = current_smallest_number
            previous_smallest_index = current_smallest_index
            current_smallest_number = math.inf
    return previous_smallest_number


# Brute Force with sorting
# Time complexity: O(N*logN)
def k_smallest_brute_sorting(arr, k):
    return sorted(arr)[k-1]


# Using Max Heap
# Time Complexity: O(K*logK) + O((N-K)*logK) = O(N*logK)
# Space Complexity: O(K)
def k_smallest_max_heap(arr, k):
    # Input k elements in the heap and traverse the remaining array and update as per max heap property.
    max_heap = []
    for i in range(k):
        max_heap.append(-1 * arr[i])
    heapify(max_heap)

    for i in range(k, len(arr)):
        if -1 * arr[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -1 * arr[i])

    return -1 * heappop(max_heap)


# Min heap
# Time Complexity: O(N*logN + K*logN)
# Space Complexity: O(N)
def k_smallest_min_heap(arr, k):
    # build min heap and pop k times
    min_heap = []
    for number in arr:
        min_heap.append(number)
    heapify(min_heap)
    for i in range(k-1):
        heappop(min_heap)
    return heappop(min_heap)


# Partition Quicksort
# Time Complexity: O(N*logn) -> O(N^2)
# Space complexity: O(1)
def k_smallest_partition(arr, k):
    return k_smallest_partition_recursive(arr, k, 0, len(arr) - 1)


def k_smallest_partition_recursive(arr, k, start, end):
    pivot = partition(arr, start, end)

    if pivot == k - 1:
        return arr[pivot]

    if pivot > k - 1:
        return k_smallest_partition_recursive(arr, k, start, pivot-1)

    return k_smallest_partition_recursive(arr, k, pivot + 1, end)


# Partition in such a way that all numbers less than pivot are before the pivot
def partition(arr, low, high):
    if low == high:
        return low
    pivot = arr[high]
    for i in range(low, high):
        if arr[i] < pivot:
            arr[low], arr[i] = arr[i], arr[low]
            low += 1
    arr[low], arr[high] = arr[high], arr[low]
    return low


# Partition using median of medians
# Time Complexity: O(N) as sorting a small array is not expensive
# Space complexity
def k_smallest_median_of_means(arr, k):
    return k_smallest_median_of_means_recursive(arr, k, 0, len(arr) - 1)


def k_smallest_median_of_means_recursive(arr, k, start, end):
    pivot = partition_median(arr, start, end)
    if pivot == k - 1:
        return arr[pivot]
    if pivot > k - 1:
        return k_smallest_partition_recursive(arr, k, start, pivot - 1)
    return k_smallest_partition_recursive(arr, k, pivot + 1, end)


def partition_median(arr, start, end):
    if start == end:
        return start

    median = median_of_medians(arr, start, end)

    for i in range(start, end):
        if arr[i] == median:
            arr[i], arr[end] = arr[i], arr[end]
            break

    pivot = arr[end]
    
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
    arr[start], arr[end] = arr[end], arr[start]
    return start


def median_of_medians(arr, low, high):
    length = high - low + 1
    if length < 5:
        return arr[low]

    # Partition into chunks of 5 elements
    partitions = [arr[i: i+5] for i in range(low, high + 1, 5)]

    # Filter partitions with just 5 elements
    relevant_partitions = filter(lambda x: len(x) == 5, partitions)

    # Sort all paritions
    sorted_partitions = [sorted(p) for p in relevant_partitions]

    # Find medians
    medians = [p[2] for p in sorted_partitions]

    return partition_median(medians, 0, len(medians) - 1)


if __name__ == '__main__':
    print(k_smallest_max_heap([5, 12, 11, -1, 12], 3))
    print(k_smallest_min_heap([5, 12, 11, -1, 12], 3))
    print(k_smallest_partition([5, 12, 11, -1, 12], 3))
    print(k_smallest_median_of_means([5, 12, 11, -1, 12], 3))




