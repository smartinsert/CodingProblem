def rotated_search(array, item, leftix=0, rightix=None):
    if rightix is None:
        rightix = len(array)
    if rightix <= leftix:
        return None
    middleix = (rightix + leftix) // 2
    left, middle = array[leftix], array[middleix]
    if item == middle:
        return middleix
    if item == left:
        return leftix
    if left > middle:
        if middle < item < left:
            return rotated_search(array, item, middleix + 1, rightix)
        else:
            return rotated_search(array, item, leftix + 1, middleix)
    elif left < item < middle:
        return rotated_search(array, item, leftix + 1, middleix)
    else:
        return rotated_search(array, item, middleix + 1, rightix)


if __name__ == '__main__':
    # rotated_search([10, 15, 20, 0, 5], 5)
    rotated_search([50, 5, 20, 30, 40], 5)