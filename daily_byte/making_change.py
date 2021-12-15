"""
Given an array that represents different coin denominations and an amount of change you need to make, return the fewest number of coins it takes to make the given amount of change.
Note: If it is not possible to create the amount of change with the coins you’re given, return -1.

Ex: Given the following denominations and amount…

coins = [1,5, 10, 25], amount = 78, return 6
Take three 25 coins and three 1 coins for a total of 6 coins.
"""


def fewest_coins_to_make_change(coins: [], amount: int) -> int:
    if not coins and amount:
        return -1
    N, M = len(coins), amount
    result = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(N+1):
        for j in range(M+1):
            if j == 0:
                result[i][j] = 0
            if i == 0:
                result[i][j] = float('inf')
            if i == 1 and j >= 1:
                if j % coins[i-1] == 0:
                    result[i][j] = j//coins[i-1]
                else:
                    result[i][j] = float('inf')

    for i in range(2, N+1):
        for j in range(1, M+1):
            if coins[i-1] <= j:
                result[i][j] = min(1 + result[i][j-coins[i-1]], result[i-1][j])
            else:
                result[i][j] = result[i-1][j]
    return result[N][M]


print(fewest_coins_to_make_change([1, 5, 10, 25], 78))




