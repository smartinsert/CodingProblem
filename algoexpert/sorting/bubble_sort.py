"""
Implement bubble sort
Perform adjacent swaps
T: O(N^2)
S: O(1)
"""


def bubble_sort(array):
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(array) - counter):
            if array[i-1] > array[i]:
                array[i], array[i-1] = array[i-1], array[i]
                is_sorted = False
        counter += 1
    return array


if __name__ == '__main__':
    print(bubble_sort([8, 5, 2, 9, 5, 6, 3]))