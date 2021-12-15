"""
Find the first non-repeating character in an array.
"""

from typing import List
import math

ALPHA_SIZE = 256


def find_first(arr: str):
    n = len(arr)
    if not n:
        return ''
    character_vector = [0] * ALPHA_SIZE
    for idx, character in enumerate(arr):
        required_index = ord(character)
        character_vector[required_index] += 1

    for idx, number in enumerate(character_vector):
        if number == 1:
            return chr(idx)
    return ''


def find_first_using_map(string: str):
    character_frequency = {}
    minimum_index = math.inf
    for idx, character in enumerate(string):
        if character not in character_frequency:
            character_frequency[character] = idx
        else:
            character_frequency[character] = -1

    for character in character_frequency.keys():
        if minimum_index > character_frequency[character] > -1:
            minimum_index = character_frequency[character]
    return string[minimum_index] if minimum_index != math.inf else ''


if __name__ == '__main__':
    print(find_first('GeeksforGeeks'))
    print(find_first_using_map('GeeksforGeeks'))
    print(find_first('GeeksQuiz'))