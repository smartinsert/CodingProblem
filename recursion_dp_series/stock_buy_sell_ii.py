"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""


class Solution:
    def maxProfit(self, prices: []) -> int:
        if len(prices) == 1:
            return 0
        # return self.derive_max_profit(prices, 0)
        return self.derive_max_profit_1(prices, 0, False)

    def derive_max_profit(self, prices, start):
        if start >= len(prices):
            return 0
        overall_max = 0
        for buy in range(start, len(prices)):
            max_profit = 0
            for sell in range(buy + 1, len(prices)):
                if prices[sell] > prices[buy]:
                    profit = self.derive_max_profit(prices, sell + 1) + prices[sell] - prices[buy]
                    max_profit = max(max_profit, profit)
            overall_max = max(overall_max, max_profit)
        return overall_max

    def derive_max_profit_1(self, prices, start, can_sell):
        if start >= len(prices):
            return 0
        buy_or_sell = self.derive_max_profit_1(prices, start + 1, not can_sell) + \
                      (prices[start] if can_sell else -prices[start])
        hold = self.derive_max_profit_1(prices, start + 1, can_sell)
        return max(buy_or_sell, hold)

    def max_profit_better(self, prices) -> int:
        if len(prices) == 1:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit


solution = Solution()

print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.max_profit_better([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
