"""
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the
second integer represents a value. Your task is to find an element from a and an element form b such that the sum of
their values is less or equal to target and as close to target as possible. Return a list of ids of selected elements.
If no pair is possible, return an empty list.

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]
"""

def optimal_utilization(a, b, target):
    if not a or not b:
        return []
    result = []
    minimum = float('inf')
    a.sort(key= lambda x: x[1])
    for i in range(len(b)):
        index = binary_search(a, target - b[i][1])
        if target - a[index][1] - b[i][1] == minimum:
            result.append([a[index][0], b[i][0]])
        elif 0 < target - a[index][1] - b[i][1] < minimum:
            minimum = target - a[index][1] - b[i][1]
            result = [[a[index][0], b[i][0]]]
    return result


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2 + 1
        if arr[mid][1] == target:
            return mid
        elif arr[mid][1] < target:
            left = mid
        elif arr[mid][1] > target:
            right = mid - 1
    return right


if __name__ == '__main__':
    # print(optimal_utilization([[1, 2], [2, 4], [3, 6]], [[1, 2]], 7))
    print(optimal_utilization([[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10))