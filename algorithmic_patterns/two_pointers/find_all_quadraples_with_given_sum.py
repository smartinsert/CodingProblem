"""
Given an array of unsorted numbers and a target number,
find all unique quadruplets in it, whose sum is equal to the target number.
"""


def quadraples_with_target_sum(arr, target):
    quadraples = []
    arr.sort()
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i+1, len(arr) - 2):
            if j > i+1 and arr[j] == arr[j - 1]:
                continue
            search_pairs(arr, target, i, j, quadraples)
    return quadraples


def search_pairs(arr, target_sum, first, second, quadraples):
    left, right = second + 1, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right] + arr[first] + arr[second]
        if target_sum == current_sum:
            quadraples.append([arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1


if __name__ == '__main__':
    print(quadraples_with_target_sum([4, 1, 2, -1, 1, -3], 1))