"""
Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space; after removing the duplicates in-place return the new length of the array.
"""


def remove_duplicates(arr):
    next_non_duplicate = 1
    i = 1
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate


"""
Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place 
and return the new length of the array.
"""


def remove_duplicates_with_key(arr, k):
    next_element = 0
    for i in range(len(arr)):
        if arr[i] != k:
            arr[next_element] = arr[i]
            next_element += 1
    return next_element


if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
    print(remove_duplicates_with_key([3, 2, 3, 6, 3, 10, 9, 3], 3))
