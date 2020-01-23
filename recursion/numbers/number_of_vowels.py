def is_vowel(character):
    character = character.lower()
    vowels = 'aeiou'
    if character in vowels:
        return 1
    return 0


def iterative_number_of_vowels(string: str) -> int:
    count = 0
    for i in range(len(string)):
        if is_vowel(string[i]):
            count += 1
    return count


def recursive_number_of_vowels(string, n):
    if n == 1:
        return is_vowel(string[0])
    return recursive_number_of_vowels(string, n - 1) + is_vowel(string[n-1])


if __name__ == '__main__':
    print(iterative_number_of_vowels('Educative'))
    print(recursive_number_of_vowels('Educative', len('Educative')))