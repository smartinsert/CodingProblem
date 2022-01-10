"""
Given a string s remove all the vowels it contains and return the resulting string.
Note: In this problem y is not considered a vowel.

Ex: Given the following string s…

s = "aeiou", return ""
Ex: Given the following string s…

s = "byte", return "byt"
Ex: Given the following string s…

s = "xyz", return "xyz"
"""


def remove_vowels(s: str) -> str:
    if not s:
        return s
    return remove(s, 0, '')


def remove(s: str, idx: int, output: str) -> str:
    if idx > len(s) - 1:
        return output
    if s[idx] in set('aeiou'):
        return remove(s, idx + 1, output + '')
    else:
        return remove(s, idx + 1, output + s[idx])


print(remove_vowels('aeiou'))
print(remove_vowels('byted'))
print(remove_vowels('xyz'))
