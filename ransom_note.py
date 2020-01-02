

def check_magazine(magazine, note):
    magazine_words = dict()
    if len(magazine) < len(note):
        return False
    for word in magazine:
        if word not in magazine_words.keys():
            magazine_words[word] = 1
        else:
            magazine_words[word] += magazine_words.get(word) + 1
    for word in note:
        if word not in magazine_words or magazine_words.get(word) <= 0:
            return False
        else:
            magazine_words[word] -= 1
    return all([x >= 0 for x in magazine_words.values()])


def check_better(magazine, note):
    d = {}
    for word in magazine:
        d.setdefault(word, 0)
        d[word] += 1

    for word in note:
        if word in d:
            d[word] -= 1
        else:
            return False

    return all([x >= 0 for x in d.values()])


if __name__ == '__main__':
    print(check_magazine(['give', 'me', 'one', 'grand', 'today', 'night'], ['give', 'one', 'grand', 'today']))
    print(check_magazine(['two', 'times', 'three', 'is', 'not', 'four'], ['two', 'times', 'two', 'is', 'four']))