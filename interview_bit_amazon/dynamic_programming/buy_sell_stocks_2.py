"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.

You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Input 1:
    A = [1, 2, 3]

Output 1:
    2

Explanation 1:
    => Buy a stock on day 0.
    => Sell the stock on day 1. (Profit +1)
    => Buy a stock on day 1.
    => Sell the stock on day 2. (Profit +1)

    Overall profit = 2
"""


def maximum_profit(prices):
    max_profit = 0
    if len(prices) == 0:
        return 0
    for i in range(1, len(prices)):
        max_profit += max(prices[i] - prices[i-1], 0)
    return max_profit


if __name__ == '__main__':
    print(maximum_profit([1, 2, 3]))
    print(maximum_profit([5, 2, 10]))

