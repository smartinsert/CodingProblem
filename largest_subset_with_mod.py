
def findLargest(arr, n):

    # We first sort the array so that all divisors
    # of a number are before it.
    arr.sort(reverse = False)

    # To store count of divisors of all elements
    divCount = [1 for i in range(n)]

    # To store previous divisor in result
    prev = [-1 for i in range(n)]

    # To store index of largest element in maximum
    # size subset
    max_ind = 0

    # In i'th iteration, we find length of chain
    # ending with arr[i]
    for i in range(1, n):
        # Consider every smaller element as previous
        # element.
        for j in range(i):
            if arr[i] % arr[j] == 0:
                if divCount[i] < divCount[j] + 1:
                    divCount[i] = divCount[j] + 1
                    prev[i] = j

                    # Update last index of largest subset if size
        # of current subset is more.
        if divCount[max_ind] < divCount[i]:
            max_ind = i

            # Print result
    k = max_ind
    while k >= 0:
        print(arr[k], end=" ")
        k = prev[k]


def get_largest_subset(arr, prev_num=1, curr_ind=0, prev_subset=[]):
    if curr_ind == len(arr):
        return prev_subset

    curr_num = arr[curr_ind]
    alt_0 = get_largest_subset(arr, prev_num, curr_ind + 1, prev_subset)
    if curr_num % prev_num == 0:
        alt_1 = get_largest_subset(
            arr, curr_num, curr_ind + 1, prev_subset + [curr_num])
        return alt_1 if len(alt_1) > len(alt_0) else alt_0

    return alt_0


if __name__ == '__main__':
    print(get_largest_subset([3, 5, 10, 20, 21]))
    print(get_largest_subset([1, 3, 6, 24]))
    print(get_largest_subset([3, 9, 15, 30]))
