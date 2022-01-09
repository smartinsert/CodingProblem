"""
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.



Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
"""


def getMaxLen(nums: []) -> int:
    if not nums:
        return 0

    if not (0 in nums):
        sum_negatives = sum([1 if n < 0 else 0 for n in nums])
        if sum_negatives and not sum_negatives % 2:
            return len(nums)
    num_reversed = nums[::-1]

    # calculate product from left or right
    for i in range(len(nums)):
        if i and nums[i] and nums[i - 1]:
            nums[i] *= nums[i - 1]
        if i and num_reversed[i] and num_reversed[i - 1]:
            num_reversed[i] *= num_reversed[i - 1]

    max_length, left, right = 0, 0, 0

    for i in range(len(nums)):
        if nums[i] == 0:
            left = 0
        else:
            left += 1
        if num_reversed[i] == 0:
            right = 0
        else:
            right += 1
        if nums[i] > 0:
            max_length = max(max_length, left)
        if num_reversed[i] > 0:
            max_length = max(max_length, right)
    return max_length
