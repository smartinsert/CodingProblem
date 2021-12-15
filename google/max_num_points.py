"""
You are given a bag of coins, an initial energy of E, and want to maximize your number of points (which starts at zero). To gain a single point you can exchange coins[i] amount of energy (i.e. if I have 100 energy and a coin that has a value 50 I can exchange 50 energy to gain a point). If you do not have enough energy you can give away a point in exchange for an increase in energy by coins[i] amount (i.e. you give away a point and your energy is increased by the value of that coin: energy += coins[i]). Return the maximum number of points you can gain.
Note: Each coin may only be used once.

Ex: Given the following coins and starting energy…

coins = [100, 150, 200] and E = 150, return 1
coins = [100,200,300,400] and E = 200, return 2
coins = [300] and E = 200, return 0
"""


def max_points(coins: [], E: int) -> int:
    if not coins:
        return 0
    if len(coins) == 1 and coins[0] > E:
        return 0
    return max_points_earned(sorted(coins), E, 0)


def max_points_earned(coins: [], E: int, score: int) -> int:
    if coins and coins[0] <= E:
        return max_points_earned(coins[1:], E-coins[0], score + 1)
    elif score > 0 and len(coins) > 1:
        return max_points_earned(coins[:-1], E+coins[-1], score - 1)
    else:
        return score


def max_points_collected(coins: [], E: int) -> int:
    if not coins:
        return 0
    if len(coins) == 1 and coins[0] > E:
        return 0
    coins.sort()
    left, right, score = 0, len(coins) - 1, 0
    while left <= right and (score or E >= coins[left]):
        if coins[left] <= E:
            E -= coins[left]
            score += 1
            left += 1
        elif left != right:
            E += coins[right]
            score -= 1
            right -= 1
        else:
            break
    return score


# print(max_points([100, 150, 200], 150))
# print(max_points([100, 200, 300, 400], 200))
# print(max_points_collected([100, 150, 200], 150))
print(max_points_collected([100, 200, 300, 400], 200))
print(max_points_collected([100, 200], 150))
