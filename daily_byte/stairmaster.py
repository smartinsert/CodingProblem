"""
Given a staircase where the ith step has a non-negative cost associated with it given by cost[i],
return the minimum cost of climbing to the top of the staircase.
You may climb one or two steps at a time and you may start climbing from either the first or second step.

Ex: Given the following cost array…

cost = [5, 10, 20], return 10.

Ex: Given the following cost array…

cost = [1, 5, 10, 3, 7, 2], return 10.
"""


def min_cost_to_climb(cost: []) -> float:
    if len(cost) < 2:
        return 0
    if len(cost) == 2:
        return cost[0]
    min_cost = float('inf')
    return min(compute_cost(cost, 0, min_cost), compute_cost(cost, 1, min_cost))


def compute_cost(cost: [], index: int, min_cost: float) -> float:
    if index >= len(cost):
        return 0
    min_cost = cost[index] + min(compute_cost(cost, index + 1, min_cost),
                                 compute_cost(cost, index + 2, min_cost))
    return min_cost


def min_cost_to_climb_1(cost: []) -> int:
    return min(compute_cost_1(cost, len(cost) - 1), compute_cost_1(cost, len(cost) - 2))


def compute_cost_1(cost: [], index: int) -> int:
    if index < 2:
        return cost[index]
    return cost[index] + min(compute_cost_1(cost, index - 1), compute_cost_1(cost, index - 2))


def minCostClimbingStairs(cost: []) -> int:
    for i in range(2, len(cost)):
        cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
    return min(cost[-1], cost[-2])


print(min_cost_to_climb([5, 10, 20]))
print(minCostClimbingStairs([5, 10, 20]))
# print(minCostClimbingStairs([5, 10, 20]))
print(min_cost_to_climb([1, 5, 10, 3, 7, 2]))


