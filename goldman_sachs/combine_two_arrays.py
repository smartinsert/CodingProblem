"""
Combine two arrays into one.
Questions:
1. Are the two arrays sorted ?
2. Do we wish to combine the array in the first one itself ?
3. Can we use a separate array to store the elements ?
4. Does the final array need to be sorted ?
"""
from typing import List
from heapq import *


# Create a new array and arrays are unsorted and final array should be sorted
def combine_two_unsorted_arrays(first_array: List[int], second_array: List[int]) -> List[int]:
    first_array = sorted(first_array)
    second_array = sorted(second_array)
    result = [0 for _ in range(len(first_array) + len(second_array))]
    i, j, k = 0, 0, 0
    while i < len(first_array) and j < len(second_array):
        if first_array[i] < second_array[j]:
            result[k] = first_array[i]
            i += 1
        else:
            result[k] = second_array[j]
            j += 1
        k += 1
    while i < len(first_array):
        result[k] = first_array[i]
        k += 1
        i += 1

    while j < len(second_array):
        result[k] = second_array[j]
        k += 1
        j += 1
    return result


def combine_two_unsorted_arrays_min_heap(first_array: List[int], second_array: List[int]) -> List[int]:
    result = list()
    [first_array.append(element) for element in second_array]
    heapify(first_array)
    while first_array:
        result.append(heappop(first_array))
    return result


if __name__ == '__main__':
    print(combine_two_unsorted_arrays([10, 5, 15], [20, 3, 2, 12]))
    print(combine_two_unsorted_arrays_min_heap([10, 5, 15], [20, 3, 2, 12]))