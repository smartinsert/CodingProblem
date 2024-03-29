"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
"""


def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:  # skip same element to avoid duplicate triplets
            continue
        search_pair(arr, -arr[i], i + 1, triplets)
    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum


def search_triplets_1(arr):
    triplets = []
    arr.sort()
    for i in range(len(arr)-1):
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return triplets


if __name__ == '__main__':
    print(search_triplets_1([-3, 0, 1, 2, -1, 1, -2]))
    # print(search_triplets([-5, 2, -1, -2, 3]))
    # print(search_triplets([-1, 0, 1, 2, -1, -4]))
