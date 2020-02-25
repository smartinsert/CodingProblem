"""
Find the smallest binary digit multiple of given number
"""


def mod(number_as_string, number):
    r = 0
    for i in range(len(number_as_string)):
        r = r*10 + int(number_as_string[i])
        r %= number
    return r


def multiple(number):
    queue, visited = [], set()
    start = '1'
    queue.append(start)

    while queue:
        current_str = queue.pop(0)

        remainder = mod(current_str, number)

        if remainder == 0:
            return current_str

        if remainder not in visited:
            visited.add(remainder)
            queue.append(current_str + '0')
            queue.append(current_str + '1')


if __name__ == '__main__':
    print(multiple(55))
    print(multiple(12))