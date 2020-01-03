

def alphabetical_id(column_number):
    alphabets = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    numbers = [i for i in range(1, 27)]
    numbers_to_alpha = dict(zip(numbers, alphabets))
    return str(numbers_to_alpha[column_number % 26] * ((column_number // 26) + 1)).upper()


if __name__ == '__main__':
    assert alphabetical_id(1) == 'A'
    assert alphabetical_id(27) == 'AA'
    assert alphabetical_id(20) == 'T'
    assert alphabetical_id(56) == 'DDD'
