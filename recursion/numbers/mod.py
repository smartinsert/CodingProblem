

def mod(dividend, divisor):
    if divisor == 0:
        return 0
    if dividend < divisor:
        return dividend
    return mod(dividend - divisor, divisor)


if __name__ == '__main__':
    print(mod(14, 12))