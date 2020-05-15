"""
Find the minimum number of coins needed to make up a sum
Time: O(n*d)
Space: O(n)
"""

import math


def minimum_coins(denominations, target):
    length = len(denominations)
    if length == 0:
        return -1
    number_of_coins = [math.inf for _ in range(target+1)]
    number_of_coins[0] = 0

    for denomination in denominations:
        for amount in range(len(number_of_coins)):
            number_of_coins[amount] = min(number_of_coins[amount], 1 + number_of_coins[amount - denomination])
    return number_of_coins[target] if number_of_coins[target] != math.inf else -1
