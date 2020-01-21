def find_all_anagrams(source, pattern):

    # Space complexity = O(N) for matched_indices and O(M) for hash map.
    window_start = 0
    char_to_frequency = {}
    matched_indices = []
    matched = 0

    # O(M) time complexity
    for character in pattern:
        if character not in char_to_frequency:
            char_to_frequency[character] = 0
        char_to_frequency[character] += 1

    # O(N) time complexity
    for window_end in range(len(source)):
        right_char = source[window_end]
        if right_char in char_to_frequency:
            char_to_frequency[right_char] -= 1
            if char_to_frequency[right_char] == 0:
                matched += 1
        if len(char_to_frequency) == matched:
            matched_indices.append(window_start)
        if window_end >= len(pattern) - 1:
            left_char = source[window_start]
            window_start += 1
            if left_char in char_to_frequency:
                if char_to_frequency[left_char] == 0:
                    matched -= 1
                    char_to_frequency[left_char] += 1
    return matched_indices


if __name__ == '__main__':
    print(find_all_anagrams('ppqp', 'pq'))
    print(find_all_anagrams('abbcabc', 'abc'))