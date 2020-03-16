"""
Generate all possible subsets in a list of elements

Input: [1, 2, 3, 5]
"""

# Use BFS


def all_subsets(numbers):
    subsets = list()
    subsets.append(list())

    for current_number in numbers:
        length = len(subsets)
        for i in range(length):
            current_set = list(subsets[i])
            current_set.append(current_number)
            subsets.append(current_set)

    return subsets


if __name__ == '__main__':
    print(all_subsets([1, 2, 3, 5]))