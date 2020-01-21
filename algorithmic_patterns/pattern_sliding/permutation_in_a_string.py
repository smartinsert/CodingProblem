def find_permutation(string, pattern):
    window_start, char_to_frequency, matched = 0, {}, 0
    for character in pattern:
        if character not in char_to_frequency:
            char_to_frequency[character] = 0
        char_to_frequency[character] += 1
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_to_frequency:
            char_to_frequency[right_char] -= 1
            if char_to_frequency[right_char] == 0:
                matched += 1
        if len(char_to_frequency) == matched:
            return True
        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            window_start += 1
            if left_char in char_to_frequency:
                if char_to_frequency[left_char] == 0:
                    matched -= 1
                char_to_frequency[left_char] += 1
    return False


if __name__ == '__main__':
    print(find_permutation('oidbcaf', 'abc'))
    print(find_permutation('odicf', 'dc'))
    print(find_permutation('bcdxabcdy', 'bcdyabcdx'))