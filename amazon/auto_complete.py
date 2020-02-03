# Python3 program to demonstrate auto-complete
# feature using Trie data structure.
# Note: This is a basic implementation of Trie
# and not the most optimized one.
from heapq import *

class TrieNode():
    def __init__(self):
        # Initialising one node for trie
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):

        # Initialising the trie structure.
        self.root = TrieNode()

    def formTrie(self, keys):

        # Forms a trie structure with the given set of strings
        # if it does not exists already else it merges the key
        # into it by extending the structure as required
        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        # Inserts a key into trie if it does not exist already.
        # And if the key is a prefix of the trie node, just
        # marks it as leaf node.
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def search(self, key):

        # Searches the given key in trie for a full match
        # and returns True on success else returns False.
        node = self.root
        found = True

        for a in list(key):
            if not node.children.get(a):
                found = False
                break

            node = node.children[a]

        return node and node.last and found

    def suggestionsRec(self, node, word, word_list):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            word_list.append(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a, word_list)

    def top_k_suggestions(self, key, k, word_list):
        word_list = []
        suggestions = []
        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return
        elif node.last and not node.children:
            suggestions.append(temp_word)
            return suggestions

        self.suggestionsRec(node, temp_word, word_list)

        heapify(word_list)
        for num_word in range(k):
            suggestions.append(heappop(word_list))
            if not word_list:
                break
        return suggestions


# Driver Code
keys = ["mobile","mouse","moneypot","monitor","mousepad"]
key = "mouse"  # key for autocomplete suggestions.
# keys1 = ['havana']
# key1 = 'havana'
t = Trie()
t.formTrie(keys)
all_suggestions = []
for i in range(1, len(key) + 1):
    suggestions = t.top_k_suggestions(key[:i], 3, [])
    all_suggestions.append(suggestions)
print(all_suggestions)
