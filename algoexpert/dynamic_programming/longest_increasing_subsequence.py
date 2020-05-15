"""
Find the longest increasing subsequence
"""


def longest_increasing_subsequence(arr):
    if len(arr) == 0:
        return []
    length = [1 for _ in range(len(arr))]
    sequences = [None for _ in range(len(arr))]
    max_length_idx = 0

    for i in range(len(arr)):
        current_number = arr[i]
        for j in range(i):
            previous_number = arr[j]
            if previous_number < current_number and length[j] + 1 > length[i]:
                length[i] = 1 + length[j]
                sequences[i] = j
            # update max_idx
            if length[i] > length[max_length_idx]:
                max_length_idx = i
    return build_sequence(arr, sequences, max_length_idx)


def build_sequence(arr, sequences, current_idx):
    result = []
    while current_idx is not None:
        result.append(arr[current_idx])
        current_idx = sequences[current_idx]
    return list(reversed(result))


def binary_search(start_idx, end_idx, indices, array, num):
    if start_idx > end_idx:
        return start_idx
    middle_idx = (start_idx + end_idx) // 2
    if array[indices[middle_idx]] < num:
        start_idx = middle_idx + 1
    else:
        end_idx = middle_idx - 1
    

if __name__ == '__main__':
    print(longest_increasing_subsequence([4, 2, 3, 6, 10, 1, 12]))


