

def minimum_edit_distance_recursive(str1: str, str2: str, m: int, n: int):
    if n == 0:
        return m
    if m == 0:
        return n
    if str1[m-1] == str2[n-1]:
        return minimum_edit_distance_recursive(str1, str2, m-1, n-1)
    return 1 + min(
        minimum_edit_distance_recursive(str1, str2, m, n - 1),  # add
        minimum_edit_distance_recursive(str1, str2, m - 1, n),  # delete
        minimum_edit_distance_recursive(str1, str2, m - 1, n - 1))  # replace


def minimum_edit_distance_dp(str1: str, str2: str):
    matrix = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])
    return matrix[len(str1)][len(str2)]


if __name__ == '__main__':
    print(minimum_edit_distance_recursive('geek', 'gesek', 4, 5))
    print(minimum_edit_distance_dp('geek', 'gesek'))
    print(minimum_edit_distance_recursive('ankit', 'mitali', 5, 6))
    print(minimum_edit_distance_dp('ankit', 'mitali'))
