"""
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
"""

from heapq import *


# Using hash map
def top_k_frequent_numbers(numbers, k):
    k_frequent_numbers = []
    number_to_frequency = {number: 0 for number in numbers}
    min_heap = []
    if not numbers:
        return []
    for number in numbers:
        number_to_frequency[number] += 1
    for number, frequency in number_to_frequency.items():
        heappush(min_heap, (frequency, number))
        if len(min_heap) > k:
            heappop(min_heap)
    while min_heap:
        k_frequent_numbers.append(heappop(min_heap)[1])
    return k_frequent_numbers


if __name__ == '__main__':
    print(top_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2))
    print(top_k_frequent_numbers([5, 12, 11, 3, 11], 2))