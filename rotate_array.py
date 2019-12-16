

def rotate(arr, d):
    res_arr = list()
    for i in range(d):
        popped = arr.pop(0)
        res_arr.append(popped)
    for i in range(len(res_arr)):
        arr.append(res_arr[i])
    return arr


if __name__ == '__main__':
    print(rotate([1, 2, 3, 4, 5], 4))