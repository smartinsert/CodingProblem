"""
Find the maximum profit with k transactions
"""

import math


def max_profit(prices, k):
    if not prices:
        return 0
    profits = [[0 for d in range(len(prices))] for t in range(k+1)]

    for i in range(1, k+1):
        max_thus_far = -math.inf
