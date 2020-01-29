"""
Given n and an array of strings, print the string that contains the digits (1, 2, 3),
if there are multiple strings that satisfies the conditions, print them in ascending order.
"""

from typing import List


def strings_with_numbers(n: int, strings: List[str]) -> List[int]:
    result = []
    for string in strings:
        if '1' in string and '2' in string and '3' in string:
            result.append(int(string))
    return sorted(result)


if __name__ == '__main__':
    for result in strings_with_numbers(5, ['1395', '1721298', '102030', '3215', '123']):
        print(result)