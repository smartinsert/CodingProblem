
def min_swaps(arr):
    arr_pos = [*enumerate(arr)]
    arr_pos.sort(key=lambda it:it[1])
    visited = {k:False for k in range(len(arr))}
    ans = 0
    for i in range(len(arr)):
        if visited[i] or arr_pos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += cycle_size - 1
    return ans


if __name__ == '__main__':
    assert min_swaps([3, 4, -2, 1, 2]) == 4