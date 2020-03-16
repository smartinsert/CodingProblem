"""
Given an array and a target number. Find indices of all two numbers that sum up to the target
arr = [0, 10, 3, 7, 1, 5, 2, 9], target = 11
"""


class Indices:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        return self.a == other.b and self.b == other.a

    def __repr__(self):
        return f'({self.a}, {self.b})'

    def __hash__(self):
        return self.a + self.b


def find_indices(arr, target):
    result = set()
    if len(arr) == 0:
        return result
    number_to_indices = {}
    for idx, number in enumerate(arr):
        number_to_indices[number] = number_to_indices.get(number, idx)

    for key in number_to_indices.keys():
        number_to_find = target - key
        if number_to_find in number_to_indices:
            indices = Indices(number_to_indices[key], number_to_indices[number_to_find])
            result.add(indices)
    return result


if __name__ == '__main__':
    print(find_indices([0, 10, 3, 7, 1, 5, 2, 9, 8], 11))