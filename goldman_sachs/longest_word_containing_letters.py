"""
Given a dictionary, and a list of letters ( or consider as a string),
find the longest word that only uses letters from the string.
"""
from typing import Set, List


def get_count_array_for(word):
    auxillary_word_count = [0 for _ in range(26)]
    for character in word:
        auxillary_word_count[ord(character) - 97] += 1
    return auxillary_word_count

def contains_all_letters(character_count, letters):
    for letter in letters:
        if character_count[ord(letter) - 97] == 0:
            return False
    return True


def sum_all_letters(character_count, letters):
    sum = 0
    for letter in letters:
        sum += character_count[ord(letter) - 97]
    return sum


def longest_word(dictionary: Set[str], letters: List[str]) -> str:
    max_length = 0
    word_with_max_length = ''
    for word in dictionary:
        if len(word) < len(letters):
            continue
        character_count = get_count_array_for(word)
        if not contains_all_letters(character_count, letters):
            continue
        if sum(character_count) - sum_all_letters(character_count, letters) > max_length:
            word_with_max_length = word
            max_length = sum(character_count) - sum_all_letters(character_count, letters)
    return word_with_max_length


if __name__ == '__main__':
    print(longest_word({"able", "ale", "apple", "bale", "kangaroo", "abasewepsadle"}, ['a', 'l']))