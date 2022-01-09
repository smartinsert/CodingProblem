def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while product >= target and left < len(arr):
            product /= arr[left]
            left += 1
        temp_result = []
        for i in range(right, left - 1, -1):
            temp_result.insert(0, arr[i])
            result.append(list(temp_result))
    return result


print(find_subarrays([2, 5, 3, 10], 50))
# print(find_subarrays([8, 2, 6, 5], 50))
