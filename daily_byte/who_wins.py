"""
Given an integer array, two players take turns picking the largest number from the ends of the array.
First, player one picks a number (either the left end or right end of the array) followed by player two.
Each time a player picks a particular numbers, it is no longer available to the other player.
This picking continues until all numbers in the array have been chosen. Once all numbers have been picked,
the player with the larger score wins. Return whether or not player one will win.
Note: You may assume that each player is playing to win (i.e. both players will always choose the maximum of the two
numbers each turn) and that there will always be a winner.
"""


def does_a_win(nums: []) -> bool:
    if not nums:
        return False
    return aggregate_score_of_a(nums, 0, len(nums) - 1) > 0


def aggregate_score_of_a(nums: [], left: int, right: int) -> int:
    if left == right:
        return nums[left]
    pick_left = nums[left] - aggregate_score_of_a(nums, left + 1, right)
    pick_right = nums[right] - aggregate_score_of_a(nums, left, right - 1)
    return max(pick_left, pick_right)


print(does_a_win([1, 2, 3]))
print(does_a_win([5, 3, 4, 5]))
print(does_a_win([3, 7, 2, 3]))
