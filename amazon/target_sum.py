"""
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a
target - 30
"""

def get_sum(numbers, target):
    numbers = [*enumerate(numbers)]
    numbers.sort(key=lambda x: x[1])
    result = []
    start, end = 0, len(numbers) - 1
    while start < end:
        number_to_find = target - 30
        current_sum = numbers[end][1] + numbers[start][1]
        if current_sum == number_to_find:
            result.append([numbers[start][0], numbers[end][0]])
            start += 1
            end -= 1
        if current_sum > number_to_find:
            end -= 1
        if current_sum < number_to_find:
            start += 1
    result = [sorted(pair) for pair in result]
    return result if len(result) == 1 else [max(result, key= lambda x: x[1])]


if __name__ == '__main__':
    print(get_sum([1, 10, 25, 35, 60], 90))
    print(get_sum([20, 50, 40, 25, 30, 10], 90))
