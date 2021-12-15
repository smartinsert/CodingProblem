"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""


def longest_subarray_with_ones_after_replacement(arr: [], k: int) -> int:
    if len(arr) < 3:
        return len(arr)
    window_start, zeroes, max_length = 0, 0, 0

    for window_end in range(len(arr)):
        right_number = arr[window_end]
        if right_number == 0:
            zeroes += 1
        if zeroes > k:
            left_number = arr[window_start]
            if left_number == 0:
                zeroes -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(longest_subarray_with_ones_after_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(longest_subarray_with_ones_after_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


