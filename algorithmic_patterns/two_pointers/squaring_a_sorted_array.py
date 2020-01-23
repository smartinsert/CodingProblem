"""
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
"""


def make_squares(arr):
    left, right = 0, len(arr) - 1
    squares = [0 for _ in range(len(arr))]
    highest_square_index = len(arr) - 1
    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square <= right_square:
            squares[highest_square_index] = right_square
            right -= 1
        elif left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
        highest_square_index -= 1
    return squares


if __name__ == '__main__':
    print(make_squares([-3, -1, 0, 1, 2]))