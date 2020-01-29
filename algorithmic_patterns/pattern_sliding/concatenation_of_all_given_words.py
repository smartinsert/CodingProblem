"""
Given a string and a list of words, find all the starting indices of substrings in the given string that are a
concatenation of all the given words exactly once without any overlapping of words.
It is given that all words are of the same length.
"""


def find_word_concatenation(source, words):
    single_word_1 = words[0] + words[1]
    single_word_2 = words[1] + words[0]
    result_indices = []
    single_word_length = len(single_word_1)
    for i in range(len(source) - single_word_length + 1):
        current_word = source[i:i + single_word_length]
        if current_word == single_word_1 or current_word == single_word_2:
            result_indices.append(i)
    return result_indices


def find_word_concatenation_1(str, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(str) - words_count * word_length) + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            # Get the next word from the string
            word = str[next_word_index: next_word_index + word_length]
            if word not in word_frequency:  # Break if we don't need this word
                break

            # Add the word to the 'words_seen' map
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:  # Store index if we have found all the words
                result_indices.append(i)

    return result_indices


def count_combinations(word):
    if len(word) <= 3:
        return 1
    return count_combinations(word[0:3]) + count_combinations(word[1:])


def total_combinations(word, sum_till_now=0):
    if len(word) < 3:
        return sum_till_now
    sum_till_now += count_combinations(word)
    return total_combinations(word[1:], sum_till_now)


if __name__ == '__main__':
    # print(find_word_concatenation_1('catfoxcat', ['cat', 'fox']))
    print(total_combinations('catfoxcat'))
