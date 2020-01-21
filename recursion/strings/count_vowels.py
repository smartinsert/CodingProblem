def foo(string):
    if not string:
        return 0
    return (1 if string[0] in 'aeiouAEIOU' else 0) + foo(string[1:])


if __name__ == '__main__':
    print(foo('thisisrecursion'))