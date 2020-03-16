"""
sort elements using quick sort
"""


def sort_elements(arr):
    n = len(arr)
    if n == 0:
        return arr
    low, high = 0, n-1
    sort_element_recursive(arr, low, high)
    return arr


def sort_element_recursive(arr, low, high):
    if low > high:
        return
    pivot = find_pivot(arr, low, high)
    sort_element_recursive(arr, low, pivot-1)
    sort_element_recursive(arr, pivot+1, high)


def find_pivot(arr, low, high):
    if low == high:
        return low
    pivot = arr[high]
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
    arr[low], arr[high] = arr[high], arr[low]
    return low


if __name__ == '__main__':
    print(sort_elements([1, 5, 12, 2, 11, 5]))