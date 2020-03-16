"""
Given an array of integers and a integer k, find number of subarrays for which median is >= k.
If numbers of elements in arrays is even then median it median will be number which is present
in index array_size/2 - 1.
"""


def has_median_k(subset, k):
    length = len(subset)
    position = length // 2 if length%2 != 0 else int(length/2 - 1)
    return subset[position] >= k


def count_subsets(numbers, k):
    count = 0
    if len(numbers) == 0:
        return count
    subsets = list()
    subsets.append(list())

    for current_number in numbers:
        n = len(subsets)
        for i in range(n):
            current_set = list(subsets[i])
            current_set.append(current_number)
            count += 1 if has_median_k(current_set, k) else 0
            subsets.append(current_set)
    return count


if __name__ == '__main__':
    print(count_subsets([3, 6, 4, 5], 4))