"""
Given a set of investment projects with their respective profits, we need to find the most profitable projects.
We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose
projects that give us the maximum profit.
"""

from heapq import *


def find_maximum_profit(project_capitals, project_profits, init_capital, num_projects):
    max_profit = 0
    if num_projects == 0:
        return max_profit

    max_profit_heap = []
    min_capital_heap = []

    for idx, capital in enumerate(project_capitals):
        heappush(min_capital_heap, (capital, idx))

    available_capital = init_capital
    for _ in num_projects:
        while min_capital_heap and min_capital_heap[0][0] <= available_capital:
            _, idx = heappop(min_capital_heap)
            heappush(max_profit_heap, -project_profits[idx])

            if not max_profit_heap:
                break

            available_capital += heappop(max_profit_heap)
    return available_capital

