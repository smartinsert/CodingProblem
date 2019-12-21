
def minimum_bribes(q):
    total_bribes = 0
    q = [p-1 for p in q]
    for current_position, expected_position in enumerate(q):
        if expected_position - current_position > 2:
            return 'Too chaotic'
        for i in range(max(0, expected_position-1), current_position):
            if q[i] > expected_position:
                total_bribes += 1


if __name__ == '__main__':
    print(minimum_bribes([2, 1, 5, 3, 4]))
    print(minimum_bribes([2, 5, 1, 3, 4]))
    print(minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4]))
