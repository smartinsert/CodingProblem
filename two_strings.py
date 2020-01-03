
def sub_strings(string_1, string_2):
    available = [False] * 26
    for character in string_1:
        available[ord(character) - 97] = True
    return any([available[ord(character) - 97] for character in string_2])


if __name__ == '__main__':
    print(sub_strings('hello', 'world'))
    print(sub_strings('hi', 'world'))
