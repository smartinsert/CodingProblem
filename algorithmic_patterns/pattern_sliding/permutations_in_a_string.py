"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


def find_permutation_naive(str1: str, pattern: str) -> bool:
    if not str1 and not pattern:
        return True
    if not str1 and pattern:
        return False
    if str1 and not pattern:
        return False
    for i in range(len(str1) - len(pattern) + 1):
        if ''.join(sorted(pattern)) == ''.join(sorted(str1[i:i+len(pattern)])):
            return True
    return False


# print(find_permutation_naive("odicf", "dc"))
# print(find_permutation_naive("oidbcaf", "abc"))
# print(find_permutation_naive("bcdxabcdy", "bcdyabcdx"))


def find_permutation(str1: str, pattern: str) -> bool:
    if not str1 and not pattern:
        return True
    if not str1 and pattern:
        return False
    if str1 and not pattern:
        return False
    window_start, matched, length_to_match = 0, 0, len(pattern)
    char_to_frequency = {}
    for character in pattern:
        if character not in char_to_frequency:
            char_to_frequency[character] = 0
        char_to_frequency[character] += 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_to_frequency:
            char_to_frequency[right_char] -= 1
            if char_to_frequency[right_char] == 0:
                matched += 1
        if window_end - window_start + 1 > length_to_match:
            left_char = str1[window_start]
            if left_char in char_to_frequency:
                if char_to_frequency[left_char] == 0:
                    matched -= 1
                char_to_frequency[left_char] += 1
            window_start += 1
        if matched == len(char_to_frequency):
            return True
    return False


# print(find_permutation("odicf", "dc"))
# print(find_permutation("oidbcaf", "abc"))
# print(find_permutation("bcdxabcdy", "bcdyabcdx"))
print(find_permutation("ppqp", "pq"))
