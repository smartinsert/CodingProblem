"""
Generate all permutations
"""


# Time: O(n!*n^2); Space: O(n!*n)
def generate_permutation(arr):
    permutations = []
    permutation_helper(arr, [], permutations)
    return permutations


def permutation_helper(arr, current_permutation, permutations):
    if not len(arr) and len(current_permutation):
        permutations.append(current_permutation)
    else:
        for i in range(len(arr)):
            new_array = arr[:i] + arr[i+1:]
            new_permutation = current_permutation + [arr[i]]
            permutation_helper(new_array, new_permutation, permutations)


# Time: O(n!*n); Space: O(n!*n)
def generate_permutation_swap(arr):
    permutations = []
    permutation_swap_helper(arr, 0, permutations)
    return permutations


def permutation_swap_helper(arr, current_index, permutations):
    if current_index == len(arr) - 1:
        permutations.append(arr.copy())
    else:
        for j in range(current_index, len(arr)):
            arr[current_index], arr[j] = arr[j], arr[current_index]
            permutation_swap_helper(arr, current_index + 1, permutations)
            arr[current_index], arr[j] = arr[j], arr[current_index]


if __name__ == '__main__':
    print(generate_permutation([1, 2, 3]))
    print(generate_permutation_swap([1, 2, 3]))

