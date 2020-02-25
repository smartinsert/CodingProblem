"""
Given n ropes of different lengths, we need to connect these ropes into one rope.
We can connect only 2 ropes at a time. The cost required to connect 2 ropes is equal to sum of their lengths.
The length of this connected rope is also equal to the sum of their lengths.
This process is repeated until n ropes are connected into a single rope.
Find the min possible cost required to connect all ropes.
"""
from heapq import heappop, heappush, heapify


def min_cost(ropes):
    if not ropes:
        return []
    ropes.sort()
    costs = []
    cost_to_connect = ropes[0] + ropes[1]
    for rope in range(2, len(ropes)):
        costs.append(cost_to_connect)
        cost_to_connect += ropes[rope]
    costs.append(cost_to_connect)
    return sum(costs)


def minCost(ropes) -> int:
    if not ropes:
        return 0
    if len(ropes) == 1:
        return ropes[0]
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        a, b = heappop(ropes), heappop(ropes)
        cost += a + b
        if ropes:
            heappush(ropes, a + b)
    return cost


if __name__ == '__main__':
    print(min_cost([8, 4, 6, 12]))
    print(minCost([8, 4, 6, 12]))
    print(min_cost([1, 2, 5, 10, 35, 89]))
