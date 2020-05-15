"""
Calculate power(x, y) when y is very large

Algorithm:
1. Store the number in an array and keep a count of it's digits
2. Multiply the number n times using the number represented in the array, update the new number and the count of digits
"""

MAX = 100000


def multiply(x, result, number_of_digits):
    carry = 0

    for i in range(number_of_digits):
        prod = result[i] * x + carry
        result[i] = prod%10
        carry = prod // 10

    while carry:
        result[number_of_digits] = carry%10
        carry //= 10
        number_of_digits += 1

    return number_of_digits


def pow(x, y):
    if y == 0:
        return 1

    result = [0] * MAX

    temp = x
    number_of_digits = 0
    while temp:
        remainder = temp%10
        result[number_of_digits] = remainder
        temp //= 10
        number_of_digits += 1

    for i in range(y-1):
        number_of_digits = multiply(x, result, number_of_digits)

    for i in range(number_of_digits-1, -1, -1):
        print(result[i], end='')


if __name__ == '__main__':
    pow(25, 100)



