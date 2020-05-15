"""
Find the maximum sum from an array without using adjacent elements
"""


#Time: O(N); Space=O(N)
def max_sum_no_adjacent(arr):
    if not len(arr):
        return 0
    if len(arr) == 1:
        return arr[0]
    max_sums = arr[:]
    max_sums[1] = max(max_sums[0], max_sums[1])
    for i in range(2, len(arr)):
        max_sums[i] = max(max_sums[i-1], max_sums[i-2] + arr[i])
    return max_sums[-1]


#Time: O(N); Space: O(1)
def max_sum_no_adjacent_better(arr):
    if not len(arr):
        return 0
    if len(arr) == 1:
        return arr[0]
    second = arr[0]
    first = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        current = max(first, second + arr[i])
        first = current
        second = first
    return first


if __name__ == '__main__':
    print(max_sum_no_adjacent([7, 10, 12, 7, 9, 14]))
    print(max_sum_no_adjacent([2, 5, 1, 3, 6, 2, 4]))