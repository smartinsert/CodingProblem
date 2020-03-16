"""
strstr - locate a substring ( needle ) in a string ( haystack ).
"""


def strStr(str_to_search, main_str):
    if not str_to_search:
        return []
    if not main_str:
        return []
    if str_to_search and not main_str:
        return []
    window_start = 0
    char_to_frequency = {}
    matched = 0
    result = []

    for character in str_to_search:
        char_to_frequency[character] = char_to_frequency.get(character, 0) + 1

    for window_end in range(len(main_str)):
        right_char = main_str[window_end]
        if right_char in char_to_frequency:
            char_to_frequency[right_char] -= 1
            if char_to_frequency[right_char] == 0:
                matched += 1
        if len(char_to_frequency) == matched:
            result.append(window_start)
        if window_end >= len(str_to_search) - 1:
            left_char = main_str[window_start]
            if left_char in char_to_frequency:
                if char_to_frequency[left_char] == 0:
                    matched -= 1
                char_to_frequency[left_char] += 1
            window_start += 1
    return result


if __name__ == '__main__':
    print(strStr('abc', 'bbcababcbca'))




