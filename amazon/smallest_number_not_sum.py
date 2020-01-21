def all_combination(arr):
    if not arr:
        return [[]]
    x = all_combination(arr[1:])
    return x + [[arr[0]] + y for y in x]


if __name__ == '__main__':
    all_combination([1, 2, 3, 10])