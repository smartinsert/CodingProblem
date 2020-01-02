def max_sum(arr, k, max_till_now):
    if len(arr) < 1:
        return max_till_now
    max_till_now += max(arr[1:k+1]) if arr[1:k+1] else 0
    max_index = arr.index(max(arr[1:k+1])) if arr[1:k+1] else len(arr)
    return max_sum(arr[max_index:len(arr)], k, max_till_now)


if __name__ == '__main__':
    arr = [3, 4, -2, 1, 2]
    print(max_sum(arr, 3, arr[0]))