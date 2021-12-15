"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""

"""
Time Complexity: O(N+M)
Space Complexity: O(M) -> Hash Map; O(N) for result list when the pattern has only one character and the string has only
that character.
"""


def find_string_anagrams(str1, pattern):
    result_indexes = []
    if not str1:
        return result_indexes
    window_start, matched, window_length = 0, 0, len(pattern)
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

        if window_end - window_start + 1 > window_length:
            left_char = str1[window_start]
            if left_char in char_to_frequency:
                if char_to_frequency[left_char] == 0:
                    matched -= 1
                char_to_frequency[left_char] += 1
            window_start += 1

        if matched == len(char_to_frequency):
            result_indexes.append(window_start)
    return result_indexes


print(find_string_anagrams("ppqp", "pq"))
print(find_string_anagrams("abbcabc", "abc"))
