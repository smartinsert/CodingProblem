"""
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation:
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk",
"kwag", "wagl"
"wagl" is repeated twice, but is included in the output once.
"""

from typing import Set


def substrings_with_k_distinct_characters_of_size_k(sequence: str, k: int) -> Set[str]:
    result = set()
    window_start = 0
    char_to_frequency = {}
    for window_end in range(len(sequence)):
        right_char = sequence[window_end]
        if right_char in char_to_frequency:
            window_start = max(window_start, char_to_frequency[right_char] + 1)
        char_to_frequency[right_char] = window_end
        if window_end - window_start + 1 == k:
            result.add(sequence[window_start: window_end + 1])
            window_start += 1
    return result


if __name__ == '__main__':
    print(substrings_with_k_distinct_characters_of_size_k('abcabc', 3))
    print(substrings_with_k_distinct_characters_of_size_k('abacab', 3))
    print(substrings_with_k_distinct_characters_of_size_k('awaglknagawunagwkwagl', 4))