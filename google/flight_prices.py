"""
A company is booking flights to send its employees to its two satellite offices A and B.
The cost of sending the ith employee to office A and office B is given by prices[i][0] and prices[i][1] respectively.
Given that half the employees must be sent to office A and half the employees must be sent to office B,
return the minimum cost the company must pay for all their employees’ flights.

Ex: Give the following prices…

prices = [[40,30],[300,200],[50,50],[30,60]], return 310
Fly the first personn to office B.
Fly the second person to office B.
Fly the third person to office A.
Fly the fourth person to office A.
"""

"""
Initial thought: sort the arrays on the basis of least price for office A, send half employees there and the remaining
ones to office B.

[[10, 50],[11, 20], [21, 30], [40, 50]]
Therefore, the min cost: 10 + 11 + 30 + 50 = 101
Can we do better ?
sort on the basis of profit margin
[[10, 50], [40, 50], [11, 20], [21, 30]] 
Send person 2, 3 to office B and 1, 4 to office A
Therefore, min cost: 20 + 30 + 40 + 10 = 100

Thus, sending employees to city    
"""


def flight_prices(prices: []) -> int:
    if not prices:
        return 0
    prices.sort(key=lambda interval: interval[1] - interval[0], reverse=True)
    total_cost = 0
    for i in range(len(prices) // 2):
        total_cost += prices[i][0]
    for i in range(len(prices) // 2, len(prices)):
        total_cost += prices[i][1]
    return total_cost


print(flight_prices([[40, 30], [300, 200], [50, 50], [30, 60]]))
print(flight_prices([[10, 50], [11, 20], [21, 30], [40, 50]]))
