"""
Given an unsorted array Arr[] and a number N.
You need to write a program to find if there exists a pair of elements in the array whose difference is N.
"""


def find_pair(arr, n):
    arr.sort()
    for i in range(len(arr)):
        if search(arr, arr[i] + n):
            return True
    return False


def search(arr, number):
    start, end = 0, len(arr)
    while start <= end:
        mid = (start + end) // 2
        if number > arr[mid]:
            start = mid + 1
        elif number < arr[mid]:
            end = mid - 1
        elif number == arr[mid]:
            return True
    return False


if __name__ == '__main__':
    print(find_pair([5, 20, 3, 2, 50, 80], 78))