"""
Check if the array has a single cycle
Time: O(N)
Space: O(1)
"""


def single_cycle_check(array):
    if not array:
        return False
    num_visited = 0
    current_idx = 0
    while num_visited < len(array):
        if num_visited > 0 and current_idx == 0:
            return False
        num_visited += 1
        current_idx = get_next_index(current_idx, array)
    return current_idx == 0


def get_next_index(current_idx, array):
    jump = array[current_idx]
    next_idx = (current_idx + jump) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)


if __name__ == '__main__':
    print(single_cycle_check([2, 3, 1, -4, -4, 2]))