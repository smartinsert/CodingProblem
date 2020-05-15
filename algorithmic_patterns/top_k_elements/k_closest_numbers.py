"""
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array.
Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
"""

from heapq import *


# Time: O(log(N) + K*log(K)); Space: O(logK)
def k_closest_numbers(arr, k, x):
    if not arr:
        return []
    number_to_difference = [(-abs(x-number), number) for number in arr]
    max_heap = []
    for i in range(len(number_to_difference)):
        heappush(max_heap, number_to_difference[i])
        if len(max_heap) > k:
            heappop(max_heap)
    return sorted([number[1] for number in max_heap])


if __name__ == '__main__':
    print(k_closest_numbers([5, 6, 7, 8, 9], 3, 7))
    print(k_closest_numbers([2, 4, 5, 6, 9], 3, 6))
    print(k_closest_numbers([2, 4, 5, 6, 9], 3, 10))