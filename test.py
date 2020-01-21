
def save_soldiers(ar):
    ar = sorted(ar, reverse=True)
    for i in range(1, len(ar)):
        if ar[i] + 1 == ar[i - 1]:
            ar[i] = 0
    return sum(ar)


def max_teams(n, ar):
    index_with_value = []
    for idx, time in enumerate(ar):
        index_with_value.append((idx, time))
    index_with_value.sort(key= lambda x: x[1])
    print(index_with_value[0][0] + 1)


if __name__ == '__main__':
    # print(save_soldiers([8, 12, 7, 3]))
    # print(save_soldiers([8, 7, 9, 10, 3]))
    max_teams(3, [1, 0, 0])
    max_teams(3, [3, 1, 0])