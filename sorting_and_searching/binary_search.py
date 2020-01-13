def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid


def binary_search_recursive(arr, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] < x:
        binary_search_recursive(arr, x, mid+1, high)
    elif arr[mid] > x:
        binary_search_recursive(arr, x, low, mid-1)
    else:
        return mid


if __name__ == '__main__':
    assert binary_search([1, 3, 4, 5, 7, 8, 9], 5) == 3
    assert binary_search_recursive([1, 3, 4, 5, 7, 8, 9], 5, 0, 6) == 3