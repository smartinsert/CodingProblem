"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]
"""


def unique_subsets(nums: []) -> [[]]:
    if not nums:
        return [[]]
    subsets = []
    subsets.append([])
    start_idx, end_idx = 0, 0
    for idx, number in enumerate(sorted(nums)):
        if idx > 0 and nums[idx] == nums[idx-1]:
            start_idx = end_idx + 1
        end_idx = len(subsets) - 1
        for j in range(start_idx, end_idx+1):
            current_subset = list(subsets[j])
            current_subset.append(number)
            subsets.append(current_subset)
    return subsets

print(unique_subsets([1, 3, 3]))
print(unique_subsets([1, 5, 3, 3]))
