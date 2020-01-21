def number_sum(string):
    if string == '':
        return 0
    return int(string[0]) + int(number_sum(string[1:]))


if __name__ == '__main__':
    print(number_sum('345'))