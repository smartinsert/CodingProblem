"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23
Output: true (23 is a happy number)
Explanations: Here are the steps to find out that 23 is a happy number
"""


def is_a_happy_number(number: int) -> bool:
    if not number:
        return False
    if number == 1:
        return True
    slow, fast = number, number
    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
        if fast == slow:
            break
    return slow == 1


def find_square_sum(number):
    sum_ = 0
    while number:
        digit = number % 10
        sum_ += digit * digit
        number //= 10
    return sum_


print(is_a_happy_number(23))
print(is_a_happy_number(12))
