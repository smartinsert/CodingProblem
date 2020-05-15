"""
Reverse words in a sentence string in place
"""


def reverse_words(sentence):
    length = len(sentence)
    if length == 0:
        return sentence

    return ' '.join(word[::-1] for word in sentence.split(' '))