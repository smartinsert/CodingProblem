"""
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
"""


class String:
    def __init__(self, length, start, end):
        self.length = length
        self.start = start
        self.end = end

    def __gt__(self, other):
        return self.length > other.length


def longest_palindromic_substring(string):
    if len(string) == 0:
        return ''
    longest_substring = longest_palindromic_substring_rec(string, 0, len(string) - 1)
    return string[longest_substring.start:longest_substring.end]


def longest_palindromic_substring_rec(string, start, end):
    if start > end:
        return String(0, start, end)
    if start == end:
        return String(1, start, end)
    if string[start] == string[end]:
        remaining_length = end - start + 1
        if remaining_length == longest_palindromic_substring_rec(string, start + 1, end - 1).length:
            return String(remaining_length + 2, start, end)
    string_1 = longest_palindromic_substring_rec(string, start+1, end)
    string_2 = longest_palindromic_substring_rec(string, start, end-1)
    return max(string_1, string_2)


if __name__ == '__main__':
    print(longest_palindromic_substring('aaaabaaa'))