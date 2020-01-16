'''
Find the villagers who will be attacked first
'''


def convert_to_decimal(binary):
    binary = int(''.join(binary))
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal += dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


if __name__ == '__main__':
    input_arr = [['110000'],
                 ['100000'],
                 ['111000'],
                 ['110000']]
    least_strength = float('inf')
    row_with_least_strength = 0
    for idx, row in enumerate(input_arr):
        defence_strength = convert_to_decimal(row)
        if defence_strength < least_strength:
            row_with_least_strength = row
            least_strength = defence_strength
    print(row_with_least_strength)