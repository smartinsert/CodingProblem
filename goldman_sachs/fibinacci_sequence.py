

def recursive_fibonacci(number):
    if number <= 1:
        return number
    return recursive_fibonacci(number-2) + recursive_fibonacci(number-1)


def iterative_fibonnaci(number):
    a = 0
    b = 1
    if number == 0:
        return a
    elif number == 1:
        return b
    for i in range(2, number + 1):
        c = a + b
        a = b
        b = c
    return b


def fibonacci_dp(number):
    dp = [0 for _ in range(number + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, number + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[number]


if __name__ == '__main__':
    print(recursive_fibonacci(9))
    print(iterative_fibonnaci(9))