def smallest_window(source, pattern):
    min_length = len(source) + 1
    matched = 0
    substr_start = 0
    window_start = 0
    char_to_frequency = {}

    for character in pattern:
        if character not in char_to_frequency:
            char_to_frequency[character] = 0
        char_to_frequency[character] += 1

    for window_end in range(len(source)):
        right_char = source[window_end]
        if right_char in char_to_frequency:
            char_to_frequency[right_char] -= 1
            if char_to_frequency[right_char] == 0:
                matched += 1

        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = source[window_start]
            window_start += 1
            if left_char in char_to_frequency:
                if char_to_frequency[left_char] == 0:
                    matched -= 1
                char_to_frequency[left_char] += 1

    if min_length > len(source):
        return ''
    return source[substr_start: substr_start+min_length]


if __name__ == '__main__':
    print(smallest_window("ADOBECODEBANC", "ABC"))