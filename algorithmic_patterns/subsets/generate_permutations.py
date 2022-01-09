"""
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
"""

from collections import deque


# TC = O(N*N!)
# SC = O(N*N!)
def find_permutations(nums):
    result = []
    if not nums:
        return result
    permutations = deque()
    permutations.append([])
    for number in nums:
        current_permutations = len(permutations)
        for _ in range(current_permutations):
            current_permutation = permutations.popleft()
            for j in range(len(current_permutation) + 1):
                new_permutation = list(current_permutation)
                new_permutation.insert(j, number)
                if len(new_permutation) == len(nums):
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)
    return result


def find_permutations_recursive(nums):
    if not nums:
        return []
    return find_permutation_helper(nums, 0, [], [])


def find_permutation_helper(nums, index, current_permutation, result):
    if index == len(nums):
        result.append(current_permutation)
    for i in range(len(current_permutation) + 1):
        new_permutation = list(current_permutation)
        new_permutation.insert(i, nums[index])
        find_permutation_helper(nums, index+1, new_permutation, result)
    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
    print("Here are all the permutations recusive: " + str(find_permutations_recursive([1, 3, 5])))


main()
