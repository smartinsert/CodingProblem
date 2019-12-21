
def min_bribes(q):
    q_pos = [*enumerate(q)]
    for i in range(len(q_pos)):
        if q_pos[i][1] - (i+1) > 2:
            return 'Too chaotic'
    q_pos.sort(key=lambda it: it[1])
    bribed = {k: False for k in range(len(q))}
    total_bribes = 0
    for i in range(len(q_pos)):
        if bribed[i] and q_pos[i][0] == i:
            continue
        j = i
        bribe_cycle = 0
        while not bribed[j]:
            bribed[j] = True
            j = q_pos[j][0]
            bribe_cycle += 1
        if bribe_cycle > 0:
            total_bribes += bribe_cycle - 1
    return total_bribes


def minimum_bribes(q):
    total_bribes = 0
    q = [p-1 for p in q]
    for current_position, expected_position in enumerate(q):
        if expected_position - current_position > 2:
            return 'Too chaotic'
        for i in range(max(0, expected_position-1), current_position):
            if q[i] > expected_position:
                total_bribes += 1
    return total_bribes


if __name__ == '__main__':
    print(minimum_bribes([2, 1, 5, 3, 4]))
    print(minimum_bribes([2, 5, 1, 3, 4]))
    print(minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4]))