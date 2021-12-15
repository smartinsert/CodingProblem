"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""


def encode_string(s: str) -> str:
    if not s or (len(s) == 1 and s[0].isalpha()):
        return s
    stack = []
    number, token = '', ''
    for character in s:
        if character.isalpha():
            token += character
        elif character.isnumeric():
            number += character
        elif character == '[':
            stack.append((token, int(number) if number else 1))
            number, token = '', ''
        else:
            previousToken, number = stack.pop()
            token = previousToken + number * token
            number = ''
    return token


print(encode_string('3[a]2[bc]'))
print(encode_string('abc3[cd]xyz'))


