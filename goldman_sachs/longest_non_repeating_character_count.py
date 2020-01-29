"""
Given a string, the task is to find maximum consecutive repeating character in string.
"""


def longest_non_repeating_character(arr: str) -> str:
    if not arr:
        return ''
    length = len(arr)
    count = 0
    result = arr[0]
    for i in range(length):
        current_count = 1
        for j in range(i, length):
            if arr[j] != arr[i]:
                break
            current_count += 1
        if current_count > count:
            count = current_count
            result = arr[i]
    return result


if __name__ == '__main__':
    print(longest_non_repeating_character('geaeaeaek'))