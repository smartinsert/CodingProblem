def print_pascal(test_variable):
    if test_variable == 0:
        return [1]
    else:
        line = [1]
        previous_line = print_pascal(test_variable - 1)
        for i in range(len(previous_line) - 1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line


if __name__ == '__main__':
    print(print_pascal(3))