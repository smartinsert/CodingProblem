"""
Find all words contained in the boggle
"""


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = word


if __name__ == '__main__':
    word = 'this'
    trie = Trie()
    trie.add(word)