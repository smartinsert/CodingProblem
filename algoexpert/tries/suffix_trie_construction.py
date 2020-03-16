"""
Trie will be represented as a dictionary of dictionary starting at an empty node
"""


class Trie:
    def __init__(self, input_string):
        self.root = {}
        self.end_symbol = '*'
        self.__construct_trie(input_string)

    # Time: O(n^2), Space: O(n^2)
    def __construct_trie(self, input_string):
        for i in range(len(input_string)):
            self.__populate_trie(i, input_string)

    def __populate_trie(self, current_idx, input_string):
        node = self.root
        for j in range(current_idx, len(input_string)):
            current_letter = input_string[j]
            if current_letter not in node:
                node[current_letter] = {}
            node = node[current_letter]
        node[self.end_symbol] = True

    # Time: O(m) where m is the length of the string; Space: O(1)
    def contains(self, string):
        if not self.root:
            return False
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.end_symbol in node


if __name__ == '__main__':
    trie = Trie('babbc')
    print(trie.contains('abbc'))
