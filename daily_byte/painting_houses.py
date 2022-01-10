"""
You are tasked with painting a row of houses in your neighborhood such that each house is painted either red, blue, or green. The cost of painting the ith house red, blue or green, is given by costs[i][0], costs[i][1], and costs[i][2] respectively. Given that you are required to paint each house and no two adjacent houses may be the same color, return the minimum cost to paint all the houses.

Ex: Given the following costs array…

costs = [[1, 3, 5],[2, 4, 6],[5, 4, 3]], return 8.
Paint the first house red, paint the second house blue, and paint the third house green.
"""


def min_cost_to_paint(costs: [[]]) -> int:
    if not costs:
        return 0
    for i in range(1, len(costs)):
        costs[i][0] += min(costs[i-1][1], costs[i-1][2])
        costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
        costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
    return min(costs[-1][0], min(costs[-1][1], costs[-1][2]))


print(min_cost_to_paint([[1, 3, 5], [2, 4, 6], [5, 4, 3]]))
