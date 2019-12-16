

def compute_sum(arr, x_start, x_end, y_start, y_end):
    x_middle_element = int((x_start + x_end) / 2)
    y_middle_element = int((y_start + y_end) / 2)
    sum_x = 0
    for i in range(x_start, x_end+1):
        if i == x_middle_element:
            continue
        for j in range(y_start, y_end+1):
            sum_x += arr[i][j]
    return sum_x + arr[x_middle_element][y_middle_element]


def compute_all_hourglass_sum(arr):
    largest_hourglass_sum = -100
    for i in range(int(len(arr)/2)+1):
        for j in range(int(len(arr[i])/2)+1):
            hourglass_sum = compute_sum(arr, i, i+2, j, j+2)
            if hourglass_sum > largest_hourglass_sum:
                largest_hourglass_sum = hourglass_sum
    return largest_hourglass_sum


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]
           ]
    print(compute_all_hourglass_sum(arr))