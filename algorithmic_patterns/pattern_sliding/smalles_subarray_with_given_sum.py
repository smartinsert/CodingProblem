def smallest_subarray_with_given_sum(s, arr):
    window_start, window_sum, min_length = 0, 0, float('inf')
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    return 0 if min_length == float('inf') else min_length


if __name__ == '__main__':
    assert smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]) == 3
