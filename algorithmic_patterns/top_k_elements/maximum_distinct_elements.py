"""
Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with
maximum distinct numbers.

Input: [7, 3, 5, 8, 5, 3, 3], and K=2
Output: 3
"""

from heapq import *


def maximum_distinct_elements(arr, k):
    if len(arr) <= 0:
        return 0
    distinct_elements = 0
    number_to_frequency = {}
    for number in arr:
        number_to_frequency[number] = number_to_frequency.get(number, 0) + 1
    min_heap = []

    for number, frequency in number_to_frequency.items():
        if frequency == 1:
            distinct_elements += 1
        else:
            heappush(min_heap, (frequency, number))

    while min_heap and k > 0:
        frequency, number = heappop(min_heap)
        # Update k by the frequency of the current number
        k -= frequency - 1
        # We have successfully removed one duplicate element
        if k >= 0:
            distinct_elements += 1
        # We have to remove some distinct elements
        if k > 0:
            distinct_elements -= k
    return distinct_elements


if __name__ == '__main__':
    print(maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2))