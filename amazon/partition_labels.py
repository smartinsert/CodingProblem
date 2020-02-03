"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each
letter appears in at most one part, and return a list of integers representing the size of these parts.
"""

from typing import *
import math

def partitions(s: str) -> List[int]:
    character_to_last_position = {}
    for idx, character in enumerate(s):
        if character not in character_to_last_position:
            character_to_last_position[character] = 0
        character_to_last_position[character] = idx
    paritions = []
    current = 0
    while current < len(s):
        last_occurence_position = character_to_last_position[s[current]]
        i = current + 1
        while i != last_occurence_position :
            last_occurence_position = max(last_occurence_position, character_to_last_position[s[i]])
            i += 1
        paritions.append(i - current + 1)
        current = i + 1
    return paritions


if __name__ == '__main__':
    print(partitions("ababcbacadefegdehijhklij"))

