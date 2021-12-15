def findMaxConsecutiveOnes(nums: []) -> int:
    if not nums:
        return 0
    if len(nums) == 1 and nums[0] == 1:
        return 1
    max_ones, ones = 0, 0
    for i in range(len(nums)):
        if nums[i] == 1:
            ones += 1
        else:
            ones = 0
        max_ones = max(max_ones, ones)
    return max_ones


def maxone(A, B):
    if len(A) < B:
        return [i for i in range(A)]
    window_start, zeroes = 0, 0
    min_left_index, corresponding_right_idx, max_length = len(A) + 1, -1, 0
    left_idx, right_idx = 0, 0
    for window_end in range(len(A)):
        if A[window_end] == 0:
            zeroes += 1
        if zeroes > B:
            if A[window_start] == 0:
                zeroes -= 1
            window_start += 1
        if window_end - window_start + 1 > max_length:
            max_length = window_end - window_start + 1
            left_idx = window_start
            right_idx = window_end
    result = [i for i in range(left_idx, right_idx + 1)]
    return result


# print(findMaxConsecutiveOnes([0, 1]))

print(maxone([1, 1, 0, 1, 1, 0, 0, 1, 1, 1], 1))