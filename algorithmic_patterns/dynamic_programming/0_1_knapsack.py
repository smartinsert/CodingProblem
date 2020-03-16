"""
* 0/1 Knapsack Problem - Given items of certain weights/values and maximum allowed weight
 * how to pick items to pick items from this set to maximize sum of value of items such that
 * sum of weights is less than or equal to maximum allowed weight.
"""


def max_value(values, weights, total_weight):
    dp = [[0 for _ in range(total_weight+1)] for _ in range(len(values)+1)]

    for i in range(len(values)+1):
        for j in range(total_weight+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue
            if j - weights[i-1] >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(values)][total_weight]


if __name__ == '__main__':
    print(max_value([22, 20, 15, 30, 24, 54, 21, 32, 18, 25], [4, 2, 3, 5, 5, 6, 9, 7, 8, 10], 30))
    print(max_value([60, 100, 120], [10, 20, 30], 50))