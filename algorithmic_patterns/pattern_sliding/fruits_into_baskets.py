

def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    char_to_frequency = {}
    for window_end in range(len(fruits)):
        right_char = fruits[window_end]
        if right_char not in char_to_frequency:
            char_to_frequency[right_char] = 0
        char_to_frequency[right_char] += 1

        while len(char_to_frequency) > 2:
            left_char = fruits[window_start]
            char_to_frequency[left_char] -= 1
            if char_to_frequency[left_char] == 0:
                del char_to_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
