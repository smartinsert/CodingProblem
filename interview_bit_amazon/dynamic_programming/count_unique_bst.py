"""
Given A, generate all structurally unique BST’s (binary search trees) that store values 1…A.
"""


def structurally_unique_bst(number):
    dp = [0 for _ in range(number + 1)]

    # Base conditions
    # There will be only one tree rooted at 0 and 1
    dp[0], dp[1] = 1, 1
    for i in range(2, number + 1):
        for j in range(1, i+1):
            dp[i] += (dp[j - 1] * dp[i - j])
    return dp[number]


if __name__ == '__main__':
    print(structurally_unique_bst(3))