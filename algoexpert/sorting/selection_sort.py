"""
Implement selection sort(Least Used)
Algorithm: Maintain two list, unsorted and sorted
T: O(N^2)
S: O(1)
"""


def insertion_sort(array):
    current_index = 0
    while current_index < len(array) - 1:
        smallest_index = current_index

