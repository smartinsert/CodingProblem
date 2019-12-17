"""
You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying
to advance to the end. You can advance at most, the number of steps that you're currently on.
Determine whether you can get to the end of the array. For example, given the array [1, 3, 1, 2, 0, 1],
we can go from indices 0 -> 1 -> 3 -> 5, so return true.
Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""


def end_reachable(arr):
    if len(arr) < 1:
        return True

    for i in range(2, len(arr) + 1):
        if arr[len(arr) - i] >= i - 1:
            return end_reachable(arr[:len(arr) - i + 1])


if __name__ == '__main__':
    assert end_reachable([1, 3, 1, 2, 0, 1])
    assert end_reachable([1, 2, 0, 1, 2])
