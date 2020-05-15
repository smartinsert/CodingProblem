"""
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def maximum_continuous_one(arr, m):
    if len(arr) == 0:
        return []
    max_size_of_subarray = 0
    zero_count = 0
    indices = []
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] == 0:
                zero_count += 1
            sub_array_size = i - j
            if sub_array_size > max_size_of_subarray and zero_count <= m:
                max_size_of_subarray = sub_array_size
            if zero_count > m:
                zero_count = 0
    return indices


def maximum_continuous_one_better(arr, m):
    window_start, window_end = 0, 0
    best_window_start, max_window_length = 0, 0
    zero_count = 0
    zeroes = []
    while window_end < len(arr):
        if zero_count <= m:
            if arr[window_end] == 0:
                zero_count += 1
            window_end += 1
        elif zero_count > m:
            if arr[window_start] == 0:
                zero_count -= 1
            window_start += 1
        window_length = window_end - window_start
        if window_length > max_window_length and zero_count <= m:
            max_window_length = window_length
            best_window_start = window_start
    for i in range(max_window_length):
        if arr[best_window_start+i] == 0:
            zeroes.append(best_window_start + i)
    return zeroes


if __name__ == '__main__':
    # print(maximum_continuous_one([1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 2))
    print(maximum_continuous_one_better([1, 0, 0, 1, 1, 0, 1, 0, 1, 1], 2))