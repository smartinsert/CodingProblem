"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent.
"""


def combinations(digits):
    result = []
    if len(digits) == 0:
        return result
    mapping = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    recursive_combination(result, digits, mapping, '', 0)
    return result


def recursive_combination(result: list, digits: str, mapping: list, current_string: str, index: int):
    if index == len(digits):
        result.append(current_string)
        return
    letters = mapping[int(digits[index])]
    for i in range(len(letters)):
        recursive_combination(result, digits, mapping, current_string + letters[i], index + 1)


if __name__ == '__main__':
    print(combinations('23'))