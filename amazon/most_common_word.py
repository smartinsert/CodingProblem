import re
from typing import List
from heapq import *


def most_common_word(paragraph: str, banned_words: List[str]):
    banned_words = {word for word in banned_words}
    paragraph = paragraph.lower().split(" ")
    word_to_frequency = dict()
    most_common_word_heap = []
    for word in paragraph:
        word = re.sub('[^a-z]', '', word)
        if word in banned_words:
            continue
        if word not in word_to_frequency:
            word_to_frequency[word] = 0
        word_to_frequency[word] += 1
    for word in word_to_frequency.keys():
        frequency = word_to_frequency.get(word)
        most_common_word_heap.append((-1*frequency, word))
    heapify(most_common_word_heap)
    return heappop(most_common_word_heap)[1]


if __name__ == '__main__':
    print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ['ball']))
