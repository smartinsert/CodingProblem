

def longest(arr, k):
    window_start, max_length, char_to_frequency = 0, 0, {}
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        if right_char not in char_to_frequency:
            char_to_frequency[right_char] = 0
        char_to_frequency[right_char] += 1

        while len(char_to_frequency) > k:
            left_char = arr[window_start]
            char_to_frequency[left_char] -= 1
            if char_to_frequency[left_char] == 0:
                del char_to_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':
    print(longest("araaci", 2))