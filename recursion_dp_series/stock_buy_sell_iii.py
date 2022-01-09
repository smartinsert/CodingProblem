"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0
"""


class Solution:
    def maxProfit(self, prices: []) -> int:
        if len(prices) == 1:
            return 0
        return self.derive_max_profit(prices, 0, 4, False)

    def derive_max_profit(self, prices, start, transactions, can_sell):
        if start >= len(prices) or transactions == 0:
            return 0
        # buy or sell
        buy_or_sell = self.derive_max_profit(prices, start + 1, transactions - 1, not can_sell) + \
              (prices[start] if can_sell else -prices[start])
        skip = self.derive_max_profit(prices, start + 1, transactions, can_sell)
        return max(buy_or_sell, skip)

    # 2-transactions
    def derive_max_profit_better(self, prices) -> int:
        cost_b1, profit_1 = prices[0], 0
        cost_b2, profit_2 = prices[0], 0
        for price in prices:
            cost_b1 = min(cost_b1, price)
            profit_1 = max(profit_1, price - cost_b1)
            cost_b2 = min(cost_b2, price - profit_1)
            profit_2 = max(profit_2, price - cost_b2)
        return profit_2

    # k-transactions
    def derive_max_profit_k_transactions(self, prices, K) -> int:
        cost, profits = [prices[0]] * (K+1), [0] * (K+1)
        for price in prices:
            for k in range(1, K+1):
                cost[k] = min(cost[k], price - profits[k-1])
                profits[k] = max(profits[k], price - cost[k])
        return profits[-1]


solution = Solution()
print(solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(solution.derive_max_profit_better([3, 3, 5, 0, 0, 3, 1, 4]))
print(solution.derive_max_profit_k_transactions([3, 3, 5, 0, 0, 3, 1, 4], 2))
print(solution.derive_max_profit_k_transactions([3, 3, 5, 0, 0, 3, 1, 4], 4))
