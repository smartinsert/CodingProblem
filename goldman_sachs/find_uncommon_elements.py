"""
Find elements which are present in first array and not in second
"""

from typing import List, Set


def using_inbuilt_methods(first_array: List[int], second_array: List[int]) -> Set[int]:
    result = set(first_array).difference(second_array)
    return result


def naive_approach(first_array: List[int], second_array: List[int]) -> Set[int]:
    result = [element for element in first_array if element not in second_array]
    return set(result)


if __name__ == '__main__':
    print(using_inbuilt_methods([1, 2, 3, 4, 5, 10], [2, 3, 1, 0, 5]))
    print(naive_approach([1, 2, 3, 4, 5, 10], [2, 3, 1, 0, 5]))