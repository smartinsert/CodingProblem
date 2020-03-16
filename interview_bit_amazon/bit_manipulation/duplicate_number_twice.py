"""
Given an array of integers, every element appears twice except for one. Find that single one.
"""


def find_the_unique_number(arr):
    n = len(arr)
    if n == 0:
        return -1
    number_to_frequency = {}
    for number in arr:
        if number not in number_to_frequency:
            number_to_frequency[number] = 0
        number_to_frequency[number] += 1
    for number in number_to_frequency.keys():
        if number_to_frequency[number] == 1:
            return number
    return -1


def find_the_unique_number_2(arr):
    n = len(arr)
    if n == 0:
        return -1
    result = arr[0]
    for number in arr[1:]:
        result ^= number
    return result


if __name__ == '__main__':
    print(find_the_unique_number([1, 2, 2, 3, 1]))
    print(find_the_unique_number_2([1, 2, 2, 3, 1]))