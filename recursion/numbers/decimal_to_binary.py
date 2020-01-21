def decimal_to_binary(test_variable):
    if test_variable <= 1:
        return str(test_variable)
    return decimal_to_binary(test_variable//2) + decimal_to_binary(test_variable % 2)


if __name__ == '__main__':
    print(decimal_to_binary(5))