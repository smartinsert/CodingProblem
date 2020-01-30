"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm}
valued coins, how many ways can we make the change? The order of coins doesn’t matter.
"""
from typing import List


def minimum_number_of_coins(coins: List[int], amount: int) -> int:
    dp = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0
    for i in range(amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])
    return dp[amount]


if __name__ == '__main__':
    print(minimum_number_of_coins([1, 2, 5], 11))