"""
We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular
index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices.
You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the
movement.

Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one
direction which means the cycle should not contain both forward and backward movements.
"""


def has_a_cycle(arr: []) -> bool:
    if len(arr) < 2:
        return True
    visited = set()
    for idx in range(len(arr)):
        fast_idx, slow_idx = idx, idx
        is_forward = arr[idx] >= 0
        while True:
            fast_idx = get_next_index(is_forward, fast_idx, arr)
            if fast_idx != -1:
                fast_idx = get_next_index(is_forward, fast_idx, arr)
            slow_idx = get_next_index(is_forward, slow_idx, arr)
            if slow_idx == -1 or fast_idx == slow_idx or fast_idx == -1 or fast_idx in visited or slow_idx in visited:
                break
        if slow_idx != -1 and fast_idx == slow_idx:
            return True
        visited.add(idx)
    return False


def get_next_index(is_forward: bool, index: int, arr: []) -> int:
    direction = arr[index] >= 0
    if is_forward != direction:
        return -1
    next_index = (index + arr[index])%len(arr)

    if next_index == index:
        return - 1
    return next_index


print(has_a_cycle([1, 2, -1, 2, 2]))
print(has_a_cycle([2, 2, -1, 2]))
print(has_a_cycle([2, 1, -1, -2]))
