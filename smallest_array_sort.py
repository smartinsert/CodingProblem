

def smallest_window_sort(arr: []) -> int:
    if len(arr) < 2:
        return len(arr)
    left, right = 0, len(arr) - 1
    while left + 1 < len(arr) and arr[left + 1] > arr[left]:
        left += 1
    if left == len(arr) - 1:
        return 0
    while right - 1 > 0 and arr[right - 1] < arr[right]:
        right -= 1
    min_sub, max_sub = get_min_max(arr, left, right)
    while left >= 1 and arr[left - 1] > min_sub:
        left -= 1
    while right <= len(arr) - 2 and arr[right + 1] < max_sub:
        right += 1
    return right - left + 1


def get_min_max(arr: [], left: int, right: int) -> (int, int):
    min_num, max_num = float('inf'), float('-inf')
    for idx in range(left, right + 1):
        if arr[idx] < min_num:
            min_num = arr[idx]
        if arr[idx] > max_num:
            max_num = arr[idx]
    return min_num, max_num


print(smallest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(smallest_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(smallest_window_sort([1, 2, 3]))
print(smallest_window_sort([3, 2, 1]))