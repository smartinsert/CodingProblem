"""
A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that
a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according
to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
"""

from heapq import heappop, heappush

start_factor_counts = {2: 2, 3: 1, 5: 1}


def get_val_from_count(factor_counts):
    total = 1
    for key in factor_counts:
        total *= key * factor_counts[key]
    return total


def populate_heap(n, heap, regular_nums):
    if len(regular_nums) >= n:
        return

    lowest_val, lowest_factors = heappop(heap)
    regular_nums.add(lowest_val)
    for key in lowest_factors:
        lf_copy = lowest_factors.copy()
        lf_copy[key] += 1
        heappush(heap, (lowest_val * key, lf_copy))

    populate_heap(n, heap, regular_nums)


def get_n_regular(n, factor_counts=dict()):
    factor_counts = start_factor_counts

    heap, regular_nums = list(), set()
    heappush(heap, (get_val_from_count(factor_counts), factor_counts))
    populate_heap(n, heap, regular_nums)

    return sorted(regular_nums)


if __name__ == '__main__':
    print(get_n_regular(10))