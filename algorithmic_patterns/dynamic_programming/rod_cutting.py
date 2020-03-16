"""
Cutting rod to maximize profit. Given available lengths and the value at which they are selling,
how will you divide the length to make maximum profit.
"""


def rod_cutting(available_lengths, price_of_each_length, length_of_the_rod):
    if length_of_the_rod == 0:
        return 0
    dp = [[0 for _ in range(length_of_the_rod + 1)] for _ in range(len(available_lengths) + 1)]

    for i in range(len(available_lengths) + 1):
        for j in range(length_of_the_rod + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue
            if j - available_lengths[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-available_lengths[i-1]] + price_of_each_length[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(available_lengths)][length_of_the_rod]


if __name__ == '__main__':
    print(rod_cutting([1, 2, 3, 4], [2, 5, 7, 8], 5))