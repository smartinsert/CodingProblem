def recursive_square_of_a_number(test_variable):
    if test_variable == 0:
        return 0
    return recursive_square_of_a_number(test_variable - 1) + 2*test_variable - 1


def iterative_square_of_a_number(test_variable):
    return test_variable * test_variable


if __name__ == '__main__':
    print(recursive_square_of_a_number(5))