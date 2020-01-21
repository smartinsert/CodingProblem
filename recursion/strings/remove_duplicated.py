def remove_duplicates(string):
    # Base case
    if not string:
        return ''
    if len(string) == 1:
        return string
    if string[0] == string[1]:
        return remove_duplicates(string[1:])
    return string[0] + remove_duplicates(string[1:])


if __name__ == '__main__':
    print(remove_duplicates('Helllllooooo'))