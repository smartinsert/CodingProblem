

def min_bribes(state):
    state_with_position = [*enumerate(state)]
    state_with_position.sort(key=lambda it: it[1])
    bribed = {b: False for b in range(len(state))}
    total_bribes = 0
    for i in range(len(state)):
        if bribed[i] and state_with_position[i][0] == i:
            continue
        elif bribed[i] and abs(state_with_position[i][0] - i) > 2:
            return 'Too chaotic'
        j = i
        cycle_size = 0
        while not bribed[j]:
            bribed[j] = True
            j = state_with_position[j][0]
            cycle_size += 1
        if cycle_size > 0:
            total_bribes += cycle_size - 1
    return total_bribes


if __name__ == '__main__':
    # print(min_bribes([2, 5, 1, 3, 4]))
    # print(min_bribes([2, 1, 5, 3, 4]))
    print(min_bribes([5, 1, 2, 3, 7, 8, 6, 4]))