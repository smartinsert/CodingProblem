"""
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to
newest, including this letter just queried) spell one of the words in the given list.
"""


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add_word(self, word):
        for i in range(len(word)):
            self._insert_substring_at(i, word)

    def _insert_substring_at(self, current_idx, word):
        node = self.root
        for j in range(current_idx, len(word)):
            letter = word[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = True


class StreamChecker:
    def __init__(self, words):
        self.history = []
        self.trie = Trie()
        for word in words:
            self.trie.add_word(word[::-1])

    def query(self, letter):
        self.history.append(letter)
        node = self.trie.root
        for i in reversed(range(len(self.history))):
            if self.history[i] not in node:
                return False
            node = node[self.history[i]]
            if self.trie.end_symbol in node:
                return True
        return False

