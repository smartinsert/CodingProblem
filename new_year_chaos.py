

def min_bribes(state):
    state_with_position = [*enumerate(state)]
    bribes = 0
    for i in range(len(state) - 1):
        if state_with_position[i][1] - 1 - i > 2:
            return 'Too chaotic'
        bribes += abs(state_with_position[i][1] - (state_with_position[i][0] + 1))
    return bribes



def merge(arr, temp, left, mid, right):
    inv_count = 0
    i = left
    j = mid
    k = left
    while i <= mid - 1 and j <= right:
        if arr[j] > arr[i]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            inv_count += mid-i
    while i <= mid - 1:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for i in range(left, right+1, 1):
        arr[i] = temp[i]
    return inv_count


def _merge_sort(arr, temp, left, right):
    inv_count = 0
    if arr[left] - 1 - left > 2:
        return 'Too chaotic'
    if right > left:
        mid = int((left+right)/2)
        inv_count = _merge_sort(arr, temp, left, mid)
        inv_count += _merge_sort(arr, temp, mid+1, right)
        inv_count += merge(arr, temp, left, mid+1, right)
    return inv_count


def count_swaps(arr):
    temp = [0 for i in range(len(arr))]
    return _merge_sort(arr, temp, 0, len(arr)-1)


def minimum_bribes(q):
    total_bribes = 0
    q = [p-1 for p in q]
    for current_position, expected_position in enumerate(q):
        if expected_position - current_position > 2:
            return 'Too chaotic'
        for i in range(max(0, expected_position-1), current_position):
            if q[i] > expected_position:
                total_bribes += 1


if __name__ == '__main__':
    print(minimum_bribes([2, 1, 5, 3, 4]))
    print(minimum_bribes([2, 5, 1, 3, 4]))
    print(minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4]))


