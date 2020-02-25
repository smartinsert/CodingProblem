"""
Write a function that takes a non-empty array of distinct integers and an integer target, If any two numbers in the
input array sum up to the target return them in an array.
"""


def twoNumberSum(array, targetSum):
    start = 0
    result = []
    if not array:
        return result
    array = sorted(array)
    while start < len(array):
        current_element = array[start]
        element_to_find = targetSum - current_element
        if element_found(element_to_find, start, array):
            result.append(current_element)
            result.append(element_to_find)
        start += 1
    return result


def element_found(element_to_find, start, arr):
    return binary_search(element_to_find, arr[start+1:])


def binary_search(element_to_find, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if element_to_find < arr[mid]:
            high = mid - 1
        elif element_to_find > arr[mid]:
            low = mid + 1
        elif element_to_find == arr[mid]:
            return True
    return False


if __name__ == '__main__':
    print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
