"""
You have a ladder of X steps. You can go up the ladder by taking either one or two steps each time.
Write a function to determine how many potential different combinations of one or two steps you could take
to the top of the ladder.
"""


def number_of_ways(number_of_steps: int) -> int:
    # base case
    if number_of_steps <= 2:
        return number_of_steps
    return number_of_ways(number_of_steps - 1) + number_of_ways(number_of_steps - 2)


def number_of_ways_dp(number_of_steps: int) -> int:
    number_of_ways = [0 for _ in range(number_of_steps + 1)]
    number_of_ways[0] = 0
    number_of_ways[1] = 1
    number_of_ways[2] = 2
    for i in range(3, number_of_steps+1):
        number_of_ways[i] = number_of_ways[i-1] + number_of_ways[i-2]
    return number_of_ways[number_of_steps]


if __name__ == '__main__':
    print(number_of_ways(5))
    print(number_of_ways_dp(5))