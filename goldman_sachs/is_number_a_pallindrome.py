"""
Write a program to know if a number is a palindrome
"""


def power_of_ten(exponent):
    return 10**exponent


def is_palindrome(number):
    original_number = number
    queue = []
    digits = 0
    while number:
        remainder = number % 10
        queue.append(remainder)
        number //= 10
        digits += 1
    reversed_number = 0
    while queue:
        poppped_digit = queue.pop(0)
        reversed_number += power_of_ten(digits - 1)*poppped_digit
        digits -= 1
    return reversed_number == original_number


if __name__ == '__main__':
    print(is_palindrome(121))