"""
Given a string, sort it based on the decreasing frequency of its characters.
"""

from heapq import *


def sort_by_frequency_decreasing(word):
    result = ''
    if not word:
        return result
    character_to_frequency = {character: 0 for character in word}
    for character in word:
        character_to_frequency[character] += 1
    max_heap = []
    for character, frequency in character_to_frequency.items():
        heappush(max_heap, (-1*frequency, character))

    while max_heap:
        current_element = heappop(max_heap)
        result += current_element[1] * -current_element[0]
    return result


if __name__ == '__main__':
    print(sort_by_frequency_decreasing('Programming'))