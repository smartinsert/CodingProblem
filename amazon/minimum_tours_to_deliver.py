"""
Given N buckets, each containing A[i] items. Given K tours within which all of the items are needed to be delivered.
It is allowed to take items from only one bucket in 1 tour. The task is to tell the minimum number of items needed to be
 delivered per tour so that all of the items can be delivered within K tours.
"""


def get_minimum(n, a, k):
    # Iterating through each possible
    # value of minimum Items
    for i in range(1, max(a) + 1):
        tours = 0
        for j in range(0, len(a)):
            if a[j] % i == 0:  # Perfectly Divisible
                tours += a[j] / i

            else:
                # Not Perfectly Divisible means required
                # tours are Floor Division + 1
                tours += a[j] // i + 1

        if tours <= k:
            # Return First Feasible Value found,
            # since it is also the minimum
            return i
    return "Not Possible"


if __name__ == '__main__':
    N = 10
    A = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    k = 50
    print(get_minimum(N, A, k))