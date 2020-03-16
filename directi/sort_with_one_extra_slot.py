"""
Given an array and an extra place to store, find the minimum cycles required to sort the array

Input: [5, 4, 2, 1, 3]
"""


def sort_with_extra_space(arr):
    arr = [0] + arr
    total_cycles = 0
    i = 1
    while len(arr) > i != arr[i]:
        found_number = arr[i]
        required_number = i
        j = i
        while arr[j] != required_number and j < len(arr):
            j += 1
        arr[0] = found_number
        arr[i] = required_number
        arr[j] = arr[0]
        arr[0] = 0
        total_cycles += 3
        i += 1
    return total_cycles, arr


if __name__ == '__main__':
    print(sort_with_extra_space([5, 4, 2, 1, 3]))