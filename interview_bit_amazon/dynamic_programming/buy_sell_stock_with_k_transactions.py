"""
Maximum profit by buying and selling a share at most k times
Prices: [10, 22, 5, 75, 65, 80]
"""


def maximum_profit_with_k_transactions(prices, k):
    n = len(prices)
    if n == 0:
        return 0
    profit = [[0 for _ in range(n+1)] for _ in range(k+1)]
    # profit[t][i] represents maximum profit using t transaction till ith day
    # profit[t][i] will be maximum if
    # 1. We do not do any transaction on ith day and make t transactions till i-1 th day
    # 2. We sell on the ith day. To sell on the ith day, we need to buy stock on any of the j [0....i-1] days
    # profit[t][i] = max(profit[t][i-1], prices[i] - prices[j] + profit[t-1][j]

    for i in range(1, n):
        for t in range(1, k+1):
            max_so_far = 0
            for j in range(i):
                max_so_far = max(max_so_far, prices[i] - prices[j] + profit[t-1][j])
            profit[t][i] = max(profit[t][i-1], max_so_far)
    return profit[k][n-1]


if __name__ == '__main__':
    print(maximum_profit_with_k_transactions([10, 22, 5, 75, 65, 80], 2))
    print(maximum_profit_with_k_transactions([1, 4, 5, 2, 4], 1))