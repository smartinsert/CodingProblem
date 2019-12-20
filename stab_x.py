

def p_stab_x(arr):
    starts, ends = zip(*arr)
    return min(ends), max(starts)


if __name__ == '__main__':
    # print(p_stab_x([(1, 4), (4, 5), (7, 9), (9, 12)]))
    print(p_stab_x([(1, 4), (9, 12), (4, 7), (5, 8), (7, 9)]))