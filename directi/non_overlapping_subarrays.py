"""
Given an array of Length N. You have to select two non overlapping K length subarrays from the given array such that
the sum of elements of selected subarrays is maximum.
Given that 2*K <= N.

Example:
arr : 5 3 7 9 10 3 1 7 9 9 9 and k = 3
Here 2 subarrays will be 7, 9, 10 and 9, 9, 9
"""


# Return the sum of array from index i to j
def get_sum(prefix_sum, i, j):
    if i == 0:
        return prefix_sum[j]
    else:
        return prefix_sum[j] - prefix_sum[i-1]


def non_overlapping_subarrays(arr, k):
    n = len(arr)
    if n == 0:
        return []

    prefix_sum = [0] * n

    prefix_sum[0] = arr[0]

    # Helps in finding window sum in O(1)
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    result_idx = (n-(2*k), n-k)

    max_sum_2_subarrays = get_sum(prefix_sum, n-(2*k), n-k-1) + get_sum(prefix_sum, n-k, n-1)

    max_sum_second_subarray_with_idx = (n-k, get_sum(prefix_sum, n-k, n-1))

    for i in range(n-(2*k)-1, -1, -1):
        second_subarray_sum = get_sum(prefix_sum, i+k, i+(2*k)-1)
        if second_subarray_sum >= max_sum_second_subarray_with_idx[1]:
            max_sum_second_subarray_with_idx = (i+k, second_subarray_sum)

        both_subarray_sum = get_sum(prefix_sum, i, i+k-1) + max_sum_second_subarray_with_idx[1]

        if both_subarray_sum > max_sum_2_subarrays:
            max_sum_2_subarrays = both_subarray_sum
            result_idx = (i, max_sum_second_subarray_with_idx[0])

    return arr[result_idx[0]: result_idx[0] + k], arr[result_idx[1]: result_idx[1] + k]


if __name__ == '__main__':
    print(non_overlapping_subarrays([5, 3, 7, 9, 10, 3, 1, 7, 9, 9, 9], 3))