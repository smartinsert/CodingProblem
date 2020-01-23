"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return the count of such triplets.
"""


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += search_pair(arr, i, target - arr[i])
    return count


"""
Given an array arr of unsorted numbers and a target sum, return all triplets in it such that
arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return the count of such triplets.
"""


def triplets_with_smaller_sum(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        search_and_add_triplet(arr, i, target - arr[i], triplets)
    return triplets


def search_pair(arr, first, target_sum):
    count = 0
    left = first + 1
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
    return count


def search_and_add_triplet(arr, first, target_sum, triplets):
    left = first + 1
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target_sum:
            for i in range(right, left, -1):
                triplets.append([arr[first], arr[left], arr[i]])
            left += 1
        else:
            right -= 1


if __name__ == '__main__':
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    print(triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))