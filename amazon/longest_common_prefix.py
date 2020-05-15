
# Time: O(NM) Space: O(M) where M is the number of strings and M is the length of the longest string
def commonPrefixUtil(str1, str2):

    result = ""
    n1 = len(str1)
    n2 = len(str2)

    # Compare str1 and str2
    i = 0
    j = 0
    while i <= n1 - 1 and j <= n2 - 1:

        if (str1[i] != str2[j]):
            break

        result += str1[i]
        i += 1
        j += 1

    return (result)


# A Function that returns the longest
# common prefix from the array of strings
def commonPrefix (arr, n):

    prefix = arr[0]

    for i in range (1, n):
        prefix = commonPrefixUtil(prefix, arr[i])

    return (prefix)


def find_minimum_length(strs):
    return min(strs, key=len)


# Time: O(NMlogM); Space: O(N)
def longest_common_prefix(strs):
    minimum_length = find_minimum_length(strs)

    low, high = 0, minimum_length - 1
    common_prefix = ''
    while low <= high:
        mid = low + (low + high) // 2
        if all_contains_prefix(strs, strs[0], low, mid):
            common_prefix += strs[0][low:mid+1]
            low = mid + 1
        else:
            high = mid - 1
    return common_prefix


def all_contains_prefix(all_strings, first_string, start, end):
    for word in all_strings:
        for j in range(start, end+1):
            if word[j] != first_string[j]:
                return False
    return True


if __name__ == '__main__':
    print(commonPrefix(['flower', 'flow', 'flight'], 3))
    print(commonPrefix(['dog', 'racecar', 'car'], 3))