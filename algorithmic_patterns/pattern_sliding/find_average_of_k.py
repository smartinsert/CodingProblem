"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
"""


def find_average(arr, k):
    result = []
    for i in range(len(arr) - k + 1):
        _sum = 0.0
        for j in range(i, i+k):
            _sum += arr[j]
        result.append(_sum/k)
    return result


def find_average_sliding(arr, k):
    result = []
    window_start, window_sum = 0, 0.0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            result.append(window_sum/k)
            window_sum -= arr[window_start]
            window_start += 1
    return result


if __name__ == '__main__':
    print(find_average([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
    print(find_average_sliding([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))