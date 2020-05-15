"""
Find the longest palindromic substring
"""


# Time: O(n^3)
def bad_longest_palindromic_substring(string):
    longest = ''
    if not string:
        return ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if len(substring) > len(longest) and is_palindrome(substring):
                longest = substring
    return longest


def is_palindrome(string):
    left_idx, right_idx = 0, len(string) - 1
    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


def longest_palindromic_substring(string):
    if not string:
        return []

    current_longest = [0, 1]

    for i in range(1, len(string)):
        odd = get_longest_palindromic_string_from(string, i-1, i+1)
        even = get_longest_palindromic_string_from(string, i-1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        current_longest = max(current_longest, longest, lambda x: x[1] - x[0])
    return current_longest


def get_longest_palindromic_string_from(string, start, end):
    while start >= 0 and end < len(string):
        if string[start] != string[end]:
            break
        start += 1
        end -= 1
    return [start+1, end]