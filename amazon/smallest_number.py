

def smallest_number(arr: list) -> int:
    result = 1
    for number in arr:
        if number > result:
            break
        result += number
    return result


if __name__ == '__main__':
    assert smallest_number([1, 2, 3, 10]) == 7
