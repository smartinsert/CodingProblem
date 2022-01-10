"""
You’ve broken into an art gallery and want to maximize the value of the paintings you steal. All the paintings you steal you place in your bag which can hold at most W pounds. Given that the weight and value of the ith painting is given by weights[i] and values[i] respectively, return the maximum value you can steal.

Ex: Given the following W, weights array and values array…

W = 10, weights = [4, 1, 3], values = [4, 2, 7], return 13.

Ex: Given the following W, weights array and values array…

W = 5, weights = [2, 4, 3], values = [3, 7, 2], return 7.

Ex: Given the following W, weights array and values array…

W = 7, weights = [1, 3, 4], values = [3, 5, 6], return 11.
"""


def max_value_stolen(weights: [], value: [], W: int) -> int:
    if not weights or not value or not W:
        return 0
    return get_max_value(weights, value, W, 0)


def get_max_value(weights: [], value: [], W: int, start: int) -> int:
    if start == len(weights):
        return 0
    max_value = 0
    if weights[start] <= W:
        max_value += max(value[start] + get_max_value(weights, value, W - weights[start], start + 1),
                         get_max_value(weights, value, W, start + 1))
    else:
        max_value += get_max_value(weights, value, W, start + 1)
    return max_value


print(max_value_stolen([4, 1, 3], [4, 2, 7], 10))
print(max_value_stolen([2, 4, 3], [3, 7, 2], 5))
print(max_value_stolen([1, 3, 4], [3, 5, 6], 7))

