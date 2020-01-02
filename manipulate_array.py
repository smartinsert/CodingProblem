

def manipulate(n, queries):
    arr = [0] * n
    for query in queries:
        start_ind = query[0] - 1
        end_ind = query[1]
        value_to_add = query[2]
        arr[start_ind] += value_to_add
        try:
            arr[end_ind] -= value_to_add
        except IndexError:
            pass
    return sum_arr(arr)


def sum_arr(arr, sum=0):
    if len(arr) == 1:
        return max(sum, sum+arr[0])
    return sum_arr(arr[1:], max(sum, sum+arr[0]))


def manipulate_better(n, queries):
    # max_sum = 0
    arr = [0] * (n + 1)
    for query in queries:
        start_ind = query[0]
        end_ind = query[1]
        value_to_add = query[2]
        arr[start_ind-1] += value_to_add
        if end_ind <= len(arr):
            arr[end_ind] -= value_to_add
    return sum_arr(arr)






if __name__ == '__main__':
    print(manipulate(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
    print(manipulate(4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]]))
    print(manipulate_better(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
    print(manipulate_better(4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]]))