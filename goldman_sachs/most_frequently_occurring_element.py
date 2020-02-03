"""
Write a piece of code to find the most frequently occurring element in an array.
"""

from typing import List
import math


def most_frequent_element(arr: List[int]) -> int:
    number_to_frequency = dict()
    maximum_occurrences = -math.inf
    for number in arr:
        if number not in number_to_frequency:
            number_to_frequency[number] = 0
        number_to_frequency[number] += 1
    for number in number_to_frequency.keys():
        maximum_occurrences = max(maximum_occurrences, number_to_frequency.get(number))
    return maximum_occurrences


if __name__ == '__main__':
    print(most_frequent_element([4, 1, 3, 5, 3, 4, 3, 6, 7, 8]))