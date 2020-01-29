import re
from typing import List
from heapq import *


class WordCount:
    def __init__(self, word):
        self.word = word
        self.count = 0

    def update_count(self):
        self.count += 1

    def __hash__(self):
        return hash(self.word)

    def __eq__(self, other):
        return self.word == other.word

    def __gt__(self, other):
        return self.count > other.count


def most_common_word(paragraph: str, banned_words: List[str]):
    banned_words = {word for word in banned_words}
    words_seen = set()
    paragraph = re.sub("[^\w\s]", "", paragraph).lower().split(" ")
    for word in paragraph:
        if word in banned_words:
            continue
        if WordCount(word) not in words_seen:
            words_seen.add(WordCount(word))
        else:
            for word in words_seen:
                print(word)
    heapify(words_seen)
    return heappop(words_seen).word if len(words_seen) > 0 else ''


if __name__ == '__main__':
    print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))