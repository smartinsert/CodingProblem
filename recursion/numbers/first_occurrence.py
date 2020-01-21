

def recursive_first_occurrence(arr, test_variable, current_index):
    if len(arr) == current_index:
        return -1
    if arr[current_index] == test_variable:
        return current_index
    return recursive_first_occurrence(arr, test_variable, current_index+1)


if __name__ == '__main__':
    print(recursive_first_occurrence([9, 8, 1, 8, 1, 7], 8, 0))