def length_of_longest_substring(arr, k):
    window_start, max_length = 0, 0
    number_to_frequency = dict()

    for window_end in range(len(arr)):
        right_number = arr[window_end]
        if right_number not in number_to_frequency:
            number_to_frequency[right_number] = 0
        number_to_frequency[right_number] += 1
        if number_to_frequency[0] > k:
            left_number = arr[window_start]
            number_to_frequency[left_number] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def length_of_longest_substring_alternate(arr, k):
    window_start, max_length, max_ones = 0, 0, 0
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones += 1
        if (window_end - window_start + 1 - max_ones) > k:
            if arr[window_start] == 1:
                max_ones -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
    print(length_of_longest_substring_alternate([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring_alternate([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))