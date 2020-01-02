

def recur_sum(arr, sum=0):
    if len(arr) == 1:
        return sum
    return recur_sum(arr[1:], max(sum, sum+arr[0]))


if __name__ == '__main__':
    arr = [3, 0, 0, 7, 0, -3, -1, -7, 0, -1]
    print(recur_sum(arr))