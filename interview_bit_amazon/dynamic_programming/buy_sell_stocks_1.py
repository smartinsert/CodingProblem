"""
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Prices: [1, 4, 5, 2, 4]
"""

import math


def max_profit_with_at_most_one_transaction(prices):
    n = len(prices)
    if n == 0:
        return 0
    difference = -math.inf
    max_so_far = prices[n-1]
    for i in range(n-2, -1, -1):
        if prices[i] > max_so_far:
            max_so_far = prices[i]
        else:
            difference = max(max_so_far - prices[i], difference)
    return difference


if __name__ == '__main__':
    print(max_profit_with_at_most_one_transaction([1, 4, 5, 2, 4]))