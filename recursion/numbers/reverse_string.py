

def iterative_reverse_string(string: str):
    reverse = ''
    length = len(string) - 1
    while length >= 0:
        reverse = reverse + string[length]
        length = length - 1
    return reverse


def recursive_reverse_string(string):
    # Base case
    if len(string) == 0:
        return string
    return recursive_reverse_string(string[1:]) + string[0]


if __name__ == '__main__':
    print(iterative_reverse_string('Educative'))
    print(recursive_reverse_string('Educative'))