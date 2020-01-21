def length(string):
    if string == '':
        return 0
    return 1 + length(string[1:])


if __name__ == '__main__':
    print(length('Educative'))