"""
You are given an array of integers, where each element represents the maximum number of steps that can be jumped going
forward from that element. Write a function to return the minimum number of jumps you must take in order to get from the
start to the end of the array.
"""


def minimum_jumps(arr):
    if len(arr) < 2:
        return 0
    start = arr[0]
    jumps = list()
    for i in range(1, min(start + 1, len(arr))):
        if arr[i] == 0:
            continue
        jumps.append(1 + minimum_jumps(arr[i:]))
    return min(jumps)


def minJumps(arr, n):
    jumps = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0):
        return float('inf')

    jumps[0] = 0

    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]


if __name__ == '__main__':
    print(minimum_jumps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]))
    print(minJumps([6, 2, 4, 0, 5, 1, 1, 4, 2, 9], 10))