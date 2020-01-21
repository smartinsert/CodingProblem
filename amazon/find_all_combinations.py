

def letter(digits: str) -> list:
    if not digits:
        return list()
    mapping = [
        '0',
        '1',
        'abc',
        'def',
        'ghi',
        'jkl',
        'mno',
        'pqrs',
        'tuv',
        'wxyz'
    ]
    result = []
    letter_combination(result, digits, "", 0, mapping)
    return result


def letter_combination(result: list, digits: str, current: str, index: int, mapping: list) -> None:
    if index == len(digits):
        result.append(current)
        return
    letters = mapping[int(digits[index])]
    for letter in letters:
        letter_combination(result, digits, current + letter, index+1, mapping)


if __name__ == '__main__':
    print(letter('23'))