"""
WAP to print if two words are anagrams
"""


def is_anagram(first_word, second_word):
    if len(first_word) != len(second_word):
        return False
    return sorted(first_word) == sorted(second_word)


if __name__ == '__main__':
    print(is_anagram('LISTEN', 'SILENT'))
    print(is_anagram('TRIANGLE', 'INTEGRAL'))