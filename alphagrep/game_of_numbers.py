

def number_game(arr: list, result=None) -> list:
    if len(arr) < 3:
        return result
    if result is None:
        result = list()
    picked_arr = arr[0:3]
    picked_arr.sort()
    result.append(picked_arr[1])
    return number_game(arr[3:] + result, result)


if __name__ == '__main__':
    # print(len(number_game([1, 2, 2, 1])))
    # print(len(number_game([3, 1, 2, 2, 1])))
    print(len(number_game([7, 2, 3, 7, 5, 6, 5])))

