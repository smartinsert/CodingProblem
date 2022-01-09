"""
Given a string s and a list of words representing a dictionary, return whether or not the entirety of s can be segmented into dictionary words.
Note: You may assume all characters in s and the dictionary are lowercase.

Ex: Given the following string s and dictionary…

s = "thedailybyte", dictionary = ["the", "daily", "byte"], return true.

Ex: Given the following string s and dictionary…

s = "pizzaplanet", dictionary = ["plane", "pizza"], return false.
"""


def can_be_formed(s: str, dictionary: []) -> bool:
    if not s and dictionary:
        return True
    if s and not dictionary:
        return False
    return start_checking_words(s, set(dictionary), 0)


def start_checking_words(s: str, dictionary: [], start) -> bool:
    if start == len(s):
        return True
    for end in range(start + 1, len(s) + 1):
        if s[start: end] in dictionary and start_checking_words(s, dictionary, end):
            return True
    return False


print(can_be_formed('thedailybyte', ["the", "daily", "byte"]))
print(can_be_formed('pizzaplanet', ["plane", "pizza"]))
