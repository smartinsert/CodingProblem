

def fibonacci(test_variable):
    if test_variable <= 1:
        return test_variable
    return fibonacci(test_variable - 1) + fibonacci(test_variable - 2)


if __name__ == '__main__':
    print(fibonacci(7))