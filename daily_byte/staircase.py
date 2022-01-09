"""
Given a staircase with N steps and the ability to climb either one or two steps at a time, return the total number of ways to arrive at the top of the staircase.

Ex: Given the following value of N…

N = 2, return 2
1 step + 1 step
2 steps
Ex: Given the following value of N…

N = 3, return 3
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
"""
from functools import lru_cache


@lru_cache
def num_ways_to_jump(N: int) -> int:
    if N < 3:
        return N
    ways = 0
    ways += num_ways_to_jump(N - 1) + num_ways_to_jump(N - 2)
    return ways


print(num_ways_to_jump(3))
print(num_ways_to_jump(4))
print(num_ways_to_jump(50))