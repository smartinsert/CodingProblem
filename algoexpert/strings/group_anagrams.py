"""
Group anagrams together
"""


# Time: O(w*n*log(n) + n*w*log(w)); Space: O(w*n); where n is the length of the longest word and w=number of words
def group_anagrams(words):
    result = []
    n = len(words)
    if n == 0:
        return result
    sorted_words = [''.join(sorted(w)) for w in words]

    indices = [x for x in range(n)]

    indices.sort(key=lambda x: sorted_words[x])

    current_anagram_group = []
    current_anagram = sorted_words[indices[0]]

    for index in indices:
        word = words[index]
        sorted_word = sorted_words[index]

        if current_anagram == sorted_word:
            current_anagram_group.append(word)
            continue

        result.append(current_anagram_group)
        current_anagram_group = [word]
        current_anagram = sorted_word
    result.append(current_anagram_group)
    return result


def group_anagrams_better(words):
    if not words:
        return []
    anagrams = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())


if __name__ == '__main__':
    print(group_anagrams(['yo', 'act', 'flop', 'tac', 'cat', 'oy', 'olfp']))
    print(group_anagrams_better(['yo', 'act', 'flop', 'tac', 'cat', 'oy', 'olfp']))

