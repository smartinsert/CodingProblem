"""
Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly
k distinct characters. If the given string doesn't have k distinct characters, return 0.
"""

def get_all_substrings(s: str, k: int) -> int:
    window_start = 0
    frequency_map = {}
    result = 0
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        while len(frequency_map) > k:
            left_char = s[window_start]
            frequency_map[left_char] -= 1
            if frequency_map[left_char] == 0:
                del frequency_map[left_char]
            window_start += 1
        result += window_end - window_start + 1
    return result


if __name__ == '__main__':
    print(get_all_substrings('pqpqs', 2) - get_all_substrings('pqpqs', 1))