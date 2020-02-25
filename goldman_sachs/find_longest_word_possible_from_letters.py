"""
Given a dictionary, and a list of letters ( or consider as a string), find the longest word that only uses letters from
the string.
"""

from typing import List
import math


def longest_word_possible(letters: str, dictionary: List[str]):
    # result = []
    max_length_word = ''
    word_to_length = {}
    max_length_words = -math.inf
    for word in dictionary:
        if word not in word_to_length:
            word_to_length[word] = 0
        word_to_length[word] = len(word)

    sorted_letters = ''.join(sorted(letters))

    for word in word_to_length:
        unique_word = set(word)
        sorted_word = ''.join(sorted(unique_word))
        if sorted_word == sorted_letters:
            if len(word) > max_length_words:
                max_length_words = len(word)
    return [max_length_word]


if __name__ == '__main__':
    letters = 'ote'
    dictionary = ['toe', 'banana', 'dogs', 'bark', 'eat', 'toes', 'eot']
    print(longest_word_possible(letters, dictionary))