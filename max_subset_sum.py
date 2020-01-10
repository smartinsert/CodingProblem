

def maxSubsetSum(arr):
    dp = list()
    dp.append(arr[0])
    dp.append(max(arr[:2]))
    for a in arr[2:]:
        dp.append(max([dp[-2]+a, a, dp[-1]]))
    return dp[-1]


def maxSubsetSumRecur(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    return max([
        arr[0],
        arr[0] + maxSubsetSum(arr[2:]),
        maxSubsetSum(arr[1:])
    ])


if __name__ == '__main__':
    print(maxSubsetSum([-2, 1, 3, -4, 5]))
    print(maxSubsetSum([3, 5, -7, 8, 10]))