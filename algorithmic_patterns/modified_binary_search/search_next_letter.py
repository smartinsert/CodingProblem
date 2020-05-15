"""
Search next letter greater than the key.
Time: O(logN)
"""


def search_next_letter_greater_than(letters, key):
    n = len(letters)
    if n == 0:
        return ''
    if key > letters[-1] or key < letters[0]:
        return letters[0]

    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key > letters[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return letters[start%n] # since the loop is running while start <= end, so at the end, start = end + 1


if __name__ == '__main__':
    print(search_next_letter_greater_than(['a', 'c', 'f', 'h'], 'f'))