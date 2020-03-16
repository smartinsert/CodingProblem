"""
Implement atoi to convert a string to an integer.
Handle
Case 1: Whitespace characters in the front: Ignore
Case 2: Negative numbers
Case 3: Garbage characters
Case 4: Integer Overflow
"""


def custom_a_to_i(string):
    if len(string) == 0:
        return 0
    sign, base, idx = 1, 0, 0
    while string[idx] == ' ':
        idx += 1

    if string[idx] == '-' or string[idx] == '+':
        sign = 1 - 2*(1 if string[idx] == '-' else 0)
        idx += 1

    while idx < len(string) and '0' <= string[idx] <= '9':
        if abs(base) > (2**31 - 1):
            if sign == 1:
                return 2**31 - 1
            else:
                return -1*(2**31 - 1)
        base = 10 * base + ord(string[idx]) - ord('0')
        idx += 1
    return base*sign


if __name__ == '__main__':
    print(custom_a_to_i(' -123'))