"""
The cost of stock on each day is given in an array A[] of size N.
Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
"""
from typing import List


def stock_buy_sell(prices: List[int]):
    current = 0
    days = []
    position = 0
    buy_index = None
    buy_price = 0
    while current < len(prices) - 2:
        if prices[current] > prices[current + 1] < prices[current + 2] and position == 0:
            buy_index = current + 1
            buy_price = prices[current + 1]
            position = 1
        elif prices[current] < prices[current + 1] and position == 0:
            buy_index = current
            buy_price = prices[current]
            position = 1
        elif prices[current + 1] < prices[current] and position == 1:
            days.append((buy_index, current))
            buy_index = current
            buy_price = prices[current]
            position = 0
        current += 1
    if buy_price != 0:
        days.append((buy_index, len(prices) - 1))
    return days


def stock_buy_sell_recursive(prices, profit=0, buyable=True):
    if len(prices) < 1:
        return profit
    price_offset = -prices[0] if buyable else prices[0]
    return max(stock_buy_sell_recursive(prices[1:], profit, buyable),
               stock_buy_sell_recursive(prices[1:], profit + price_offset, not buyable))


if __name__ == '__main__':
    print(stock_buy_sell([100, 180, 260, 310, 40, 535, 695]))
    print(stock_buy_sell([23,13, 25, 29, 33, 19, 34, 45, 65, 67]))
    # print(stock_buy_sell_recursive([23, 13, 25, 29, 33, 19, 34, 45, 65, 67]))