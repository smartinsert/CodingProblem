def decimal_to_binary(test_variable):
    if test_variable <= 1:
        return str(test_variable)
    return decimal_to_binary(test_variable//2) + decimal_to_binary(test_variable % 2)


def all_binary_combinations(number):
    for i in range(number**2 - 1):
        yield decimal_to_binary(i)


if __name__ == '__main__':
    # print(decimal_to_binary(5))
    print(all_binary_combinations(3))