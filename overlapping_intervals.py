def get_min_removals(intervals, reserved_intervals, removed=0):
    print(reserved_intervals)

    if not intervals:
        return removed

    curr_interval = intervals[0]
    if_removed = get_min_removals(
        intervals[1:], reserved_intervals, removed + 1)

    for ri in reserved_intervals:
        if curr_interval[0] in ri or curr_interval[1] in ri:
            return if_removed

    new_reserved_intervals = reserved_intervals + \
                             [range(curr_interval[0], curr_interval[1])]

    return min(if_removed, get_min_removals(intervals[1:], new_reserved_intervals, removed))


if __name__ == '__main__':
    print(get_min_removals([(7, 9), (2, 4), (5, 8), (1, 3)], list()))
