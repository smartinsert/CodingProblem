"""
WAP to get the minimum trials to drop the egg such that it does not break
Given n eggs and k floors
"""
import math


def minimum_trials_to_drop_egg_recursive(number_of_eggs: int, number_of_floors: int) -> int:
    # No need for any trials if the number of eggs are zero
    if number_of_eggs == 0:
        return 0
    if number_of_floors == 0 or number_of_floors == 1:
        return number_of_floors
    if number_of_eggs == 1:
        return number_of_floors
    minimum_trials = math.inf
    for current_floor in range(1, number_of_floors + 1):
        trials = max(
            minimum_trials_to_drop_egg_recursive(number_of_eggs - 1, current_floor - 1),  # Egg breaks
            minimum_trials_to_drop_egg_recursive(number_of_eggs, number_of_floors - current_floor)  # Egg doesnt break
        )
        minimum_trials = min(minimum_trials, trials)
    return 1 + minimum_trials


def minimum_floor_to_drop_egg_dynamic_programming(number_of_eggs: int, number_of_floors: int) -> int:
    # rows are eggs and columns are floors
    dp = [[0 for _ in range(number_of_floors+1)] for _ in range(number_of_eggs + 1)]
    # When there is zero or one floor
    for i in range(number_of_eggs + 1):
        dp[i][0] = 0
        dp[i][1] = 1
    # When there is one egg
    for i in range(number_of_floors + 1):
        dp[1][i] = i

    for egg in range(2, number_of_eggs + 1):
        for floor in range(2, number_of_floors + 1):
            dp[egg][floor] = math.inf
            for current_floor in range(1, floor + 1):
                trials = 1 + max(dp[egg-1][current_floor-1], dp[egg][floor - current_floor])
                dp[egg][floor] = min(dp[egg][floor], trials)
    return dp[number_of_eggs][number_of_floors]


if __name__ == '__main__':
    # print(minimum_trials_to_drop_egg_recursive(2, 10))
    print(minimum_floor_to_drop_egg_dynamic_programming(2, 100))