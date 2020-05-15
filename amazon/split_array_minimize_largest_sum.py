"""
Split the array into m contiguous parts and minimize the maximum sum
"""


# If the entire array is considered as a single piece, the max sum would be sum(nums)
# If the entire array such that each element is it's own subarray then max sum would be max(num)
# Lower bound will be the maximum number and the upper bound
def split_array(nums, m):
    if len(nums) == 0:
        return 0
    lower_bound = max(nums)
    upper_bound = sum(nums)

    while lower_bound < upper_bound:
        middle = lower_bound + (upper_bound - lower_bound) // 2
        pieces = split(nums, middle)
        if pieces > m:
            lower_bound = middle + 1
        else:
            upper_bound = middle
    return lower_bound


def split(nums, largest_sum):
    pieces = 1
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum > largest_sum:
            pieces += 1
            current_sum = num
    return pieces


if __name__ == '__main__':
    print(split_array([7, 2, 5, 10, 8], 2))