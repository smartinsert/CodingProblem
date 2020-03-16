"""
Implement insertion sort
T: O(N^2)
S: O(1)
"""


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array


if __name__ == '__main__':
    print(insertion_sort([8, 5, 2, 9, 5, 6, 3]))