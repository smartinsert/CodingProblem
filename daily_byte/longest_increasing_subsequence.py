"""
Given an array of unsorted integers, return the length of its longest increasing subsequence.
Note: You may assume the array will only contain positive numbers.

Ex: Given the following array nums…

nums = [1, 9, 7, 4, 7, 13], return 4.
The longest increasing subsequence is 1, 4, 7, 13.
"""


def longest_increasing_subsequence_naive(nums: []) -> int:
    if len(nums) < 2:
        return len(nums)
    max_length = 0
    for i in range(len(nums)):
        length = 1
        for j in range(i + 1, len(nums)):
            if j + 1 < len(nums) and nums[i] < nums[j] < nums[j + 1]:
                length += 1
            # if j + 1 < len(nums) and nums[i] < nums[j] < nums[j - 1] and nums[j] < nums[j + 1]:
            #     length += 1
            elif j + 1 == len(nums) and nums[j] > nums[i]:
                length += 1
        max_length = max(max_length, length)
    return max_length


def lengthOfLIS(nums: []) -> int:
    if not nums:
        return 0
    ret = 0
    for i in range(len(nums)):
        nxt = []
        for j in range(i + 1, len(nums)):
            # Bigger than ith element, put it into next recur call
            if nums[i] < nums[j]:
                nxt.append(nums[j])

        # Call next recursive
        # + 1 meaning is the next round can increase the result length
        ret = max(ret, lengthOfLIS(nxt) + 1)

    return ret


# print(longest_increasing_subsequence([1, 9, 7, 4, 7, 13]))
# print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))
# print(longest_increasing_subsequence_naive([0, 1, 0, 3, 2, 3]))
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))
# print(longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]))
