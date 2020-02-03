"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
"""


def spiral_matrix(number):
    result = [[-1 for _ in range(number)] for _ in range(number)]
    k = 1
    top = 0
    bottom = number - 1
    left = 0
    right = number - 1

    while k <= number * number:
        for i in range(left, right+1):
            result[top][i] = k
            k += 1

        top += 1

        for i in range(top, bottom + 1):
            result[i][right] = k
            k += 1

        right -= 1

        for i in range(right, left - 1, -1):
            result[bottom][i] = k
            k += 1

        bottom -= 1

        for i in range(bottom, top-1, -1):
            result[i][left] = k
            k += 1

        left += 1

    return result


if __name__ == '__main__':
    print(spiral_matrix(3))