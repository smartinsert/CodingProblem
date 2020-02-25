"""
Design an algorithm to find the maximum profit. You may complete at most 2 transactions.
"""


def maximum_profit(prices):
    if len(prices) == 0:
        return 0
    max_profit = 0
    for i in range(1, len(prices)):
        max_profit += max(max_profit, prices[i] - prices[i-1])
    return max_profit


def maximum_profit_with_atmost_2_transactions(prices):
    max_profit = 0
    for i in range(len(prices)):
        max_profit = maximum_profit(prices[:i]) + maximum_profit(prices[i:])
    return max_profit


def maximum_profit_with_atmost_2_transactions_memoization(prices):
    n = len(prices)
    profit = [0 for _ in range(n)]

    max_price = prices[n-1]
    for i in range(n-2, -1, -1):
        # Update max_price
        if prices[i] > max_price:
            max_price = prices[i]
        profit[i] = max(profit[i+1], max_price - prices[i])

    min_price = prices[0]
    for i in range(1, n):
        if prices[i] < min_price:
            min_price = prices[i]
        profit[i] = max(profit[i-1], profit[i] + prices[i] - min_price)
    return profit[n-1]


if __name__ == '__main__':
    print(maximum_profit_with_atmost_2_transactions([1, 2, 1, 2]))
    print(maximum_profit_with_atmost_2_transactions([7, 2, 4, 8, 7]))
    print(maximum_profit_with_atmost_2_transactions_memoization([7, 2, 4, 8, 7]))