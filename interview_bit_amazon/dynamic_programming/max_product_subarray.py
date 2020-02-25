"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
Input : [2, 3, -2, 4]
Return : 6

Possible with [2, 3]
"""


def max_product_subarray(arr):
    max_value, min_value, max_product = arr[0], arr[0], arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_value, min_value = min_value, max_value
        max_value = max(max_value, max_value * arr[i])
        min_value = min(min_value, min_value * arr[i])
        max_product = max(max_product, max_value)
    return max_product


def max_contiguous_product_subarray(arr):
    max_ending_here = 1
    min_ending_here = 1

    max_so_far = 1

    for i in range(0, len(arr)):
        if arr[i] > 0:
            max_ending_here = max_ending_here * arr[i]
            min_ending_here = min(1, min_ending_here * arr[i])
        elif arr[i] == 0:
            max_ending_here, min_ending_here = 1, 1
        else:
            temp = max_ending_here
            max_ending_here = max(1, min_ending_here * arr[i])
            min_ending_here = temp * arr[i]
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


if __name__ == '__main__':
    print(max_product_subarray([2, 3, -2, 4]))
    print(max_contiguous_product_subarray([2, 3, -2, 4]))