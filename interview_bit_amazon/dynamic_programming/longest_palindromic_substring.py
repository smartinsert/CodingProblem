"""
Given a string, find the length of its Longest Palindromic Substring (LPS).
In a palindromic string, elements read the same backward and forward.
"""


def longest_palindromic_substring(string):
    return longest_palindromic_substring_util(string, 0, len(string) - 1)


def longest_palindromic_substring_util(string, start, end):
    if start > end:
        return 0

    # All strings of unit length are palindrome
    if start == end:
        return 1

    if string[start] == string[end]:
        remaining_length = end - start - 1
        # Check if the remaining string is also a palindrome
        if remaining_length == longest_palindromic_substring_util(string, start + 1, end - 1):
            return remaining_length + 2

    # Remove character from front and check
    length_1 = longest_palindromic_substring_util(string, start + 1, end)
    # Remove character from end and check
    length_2 = longest_palindromic_substring_util(string, start, end - 1)
    return max(length_1, length_2)


if __name__ == '__main__':
    print(longest_palindromic_substring('abba'))

