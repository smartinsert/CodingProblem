def gcd(test_variable_1, test_variable_2):
    if test_variable_1 == test_variable_2:
        return test_variable_1
    if test_variable_1 > test_variable_2:
        return gcd(test_variable_1 - test_variable_2, test_variable_2)
    else:
        return gcd(test_variable_1, test_variable_2 - test_variable_1)


if __name__ == '__main__':
    print(gcd(5, 2))