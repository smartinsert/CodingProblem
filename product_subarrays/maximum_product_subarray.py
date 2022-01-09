"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


def max_product_subarray(nums: []):
    if not nums:
        return 0
    current_min, current_max, result = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        compare = (current_min * nums[i], current_max * nums[i], nums[i])
        current_max, current_min = max(compare), min(compare)
        result = max(result, current_max)
    return result


def max_product_subarray_another(nums: []):
    if not nums:
        return 0
    max_product = 0
    for i in range(len(nums)):
        product = nums[i]
        for j in range(i + 1, len(nums)):
            product *= nums[j]
            max_product = max(max_product, product)
    return max_product


print(max_product_subarray([2, 3, -2, 4]))
print(max_product_subarray([-2, 0, -1]))
print(max_product_subarray_another([-2, 0, -1]))
print(max_product_subarray_another([2, 3, -2, 4]))
