def dutch_flag_sort(arr):
    # all elements < low are 0, and all elements > high are 2
    # all elements from >= low < i are 1
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            # increment 'i' and 'low'
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:  # the case for arr[i] == 2
            arr[i], arr[high] = arr[high], arr[i]
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            high -= 1


def dutch_flag(arr):
    if len(arr) < 2:
        return arr
    i, low, high = 0, 0, len(arr) - 1
    while i <= high:
        if arr[i] == 0:
            arr[low], arr[i] = arr[i], arr[low]
            low += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[high], arr[i] = arr[i], arr[high]
            high -= 1
    return arr


def main():
    # arr = [1, 0, 2, 1, 0]
    # # dutch_flag_sort(arr)
    # print(dutch_flag(arr))
    # print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    print(dutch_flag(arr))
    # print(arr)


main()
