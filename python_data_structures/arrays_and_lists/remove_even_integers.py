"""
Given an array of size n, remove all even integers from it.
Implement this solution in Python and see if it runs without an error.
"""


def remove_even_integers(arr):
    arr = [element for element in arr if element%2 != 0]
    return arr


if __name__ == '__main__':
    print(remove_even_integers([1,2,4,5,10,6,3]))