"""
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter,
find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""


def longest_substring_with_replacement(str1: str, k: int) -> int:
    if not str1:
        return 0
    window_start, max_repeating_letter_count, max_length = 0, 0, 0
    char_to_frequency = {}
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_to_frequency:
            char_to_frequency[right_char] = 0
        char_to_frequency[right_char] += 1

        max_repeating_letter_count = max(max_repeating_letter_count, char_to_frequency[right_char])

        if (window_end - window_start + 1) - max_repeating_letter_count > k:
            left_char = str1[window_start]
            char_to_frequency[left_char] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(longest_substring_with_replacement('aabccbb', 2))
print(longest_substring_with_replacement('abbcb', 1))
print(longest_substring_with_replacement('abbcb', 0))



