"""
 A ship is about to set sail and you are responsible for its safety precautions. More specifically, you are responsible
 for determining how many life rafts to carry onboard. You are given a list of all the passengers’ weights and
 are informed that a single life raft has a maximum capacity of limit and can hold at most two people.
 Return the minimum number of life rafts you must take onboard to ensure the safety of all your passengers.
 Note: You may assume that a the maximum weight of any individual is at most limit.

 Ex: Given the following passenger weights and limit…

    weights = [1, 3, 5, 2] and limit = 5, return 3
    weights = [1, 2] and limit = 3, return 1
    weights = [4, 2, 3, 3] and limit = 5 return 3
"""

"""
Two pointer approach
"""


def min_life_rafts(weights: [], limit: int) -> int:
    if not weights:
        return 0
    if not limit:
        return int('inf')
    weights.sort()
    left, right, count = 0, len(weights) - 1, 0
    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        count += 1
    return count


print(min_life_rafts([1, 3, 5, 2], 5))
print(min_life_rafts([1, 2], 3))
print(min_life_rafts([4, 2, 3, 3], 5))
