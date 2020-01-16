

def k_largest(arr: list, k):
    arr.sort(reverse=True)
    return arr[:k]


if __name__ == '__main__':
    print(k_largest([12, 5, 787, 1, 23], 2))