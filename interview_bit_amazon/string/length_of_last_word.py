"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Given s = "Hello World",

return 5 as length("World") = 5.
"""


def length_of_the_last_word(string):
    if len(string) == 0:
        return 0

    length, idx = 0, 0

    while string[idx] == ' ':
        idx += 1

    while idx < len(string):
        length += 1
        if string[idx] == ' ':
            length = 0
        idx += 1
    return length


if __name__ == '__main__':
    print(length_of_the_last_word('Hello World'))