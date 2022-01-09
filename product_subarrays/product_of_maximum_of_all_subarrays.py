"""
Given an array arr[] consisting of N positive integers, the task is to find the product of the maximum of all possible
subsets of the given array. Since the product can be very large, print it to modulo (10^9 + 7)
"""


def max_product_of_subarrays(arr: []) -> int:
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    all_subsets = generate_subsets(arr)
    product = 1
    for subset in all_subsets:
        product *= max(subset) if subset else 1
    return product


def generate_subsets(arr: []) -> []:
    if not arr:
        return [[]]
    element = generate_subsets(arr[1:])
    return element + [[arr[0]] + y for y in element]


def max_product_of_subarrays_better(arr: []) -> int:
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    product = 1
    mod = 10**9 + 7
    arr.sort()
    for i in range(len(arr) - 1, -1, -1):
        times = 2**i - 1 if i > 0 else 1

        for _ in range(times):
            product *= arr[i]
            product %= mod
    # consider subset of size 1
    for i in range(len(arr)):
        product *= arr[i]

    return product




arr = [1, 2, 3]
# print(max_product_of_subarrays(arr))
print(max_product_of_subarrays_better(arr))
# print(maximumProduct(arr, len(arr)))

