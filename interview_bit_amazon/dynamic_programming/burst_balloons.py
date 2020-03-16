"""
Given n balloons, indexed from 0 to n-1.
Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
"""

from typing import List


def maximum_coins(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    length = len(nums)

    dp = [[0 for _ in range(length)] for _ in range(length)]

    def calculate(start, end):
        if start > end:
            return dp[start][end]
        elif dp[start][end]:
            return dp[start][end]
        else:
            max_coins = 0
            for k in range(start, end+1):
                left = nums[start-1]
                right = nums[end+1]
                coins_k_max = calculate(start, k-1) + left * nums[k] * right + calculate(k+1, end)
                max_coins = max(max_coins, coins_k_max)
            dp[start][end] = max_coins
            return dp[start][end]
    return calculate(1, length-2)


if __name__ == '__main__':
    print(maximum_coins([3, 1, 5, 8]))