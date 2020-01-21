def replace_occurrences(string, a, b):
    if not string:
        return ''
    if string[:len(b)] == b:
        return a + replace_occurrences(string[len(b):], a, b)
    return string[0] + replace_occurrences(string[1:], a, b)


if __name__ == '__main__':
    print(replace_occurrences('name is ankit', 'mitali', 'name'))
