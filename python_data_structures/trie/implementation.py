from heapq import *


class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26
        self.is_end_word = False
        self.char = char

    def mark_as_leaf(self):
        self.is_end_word = True

    def unmark_as_leaf(self):
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t):
        return ord(t) - ord('a')

    def insert(self, key):
        if not key:
            return
        key = key.lower()
        current_node = self.root
        index = 0
        for level in range(len(key)):
            index = self.get_index(key[level])
            if not current_node.children[index]:
                current_node.children[index] = TrieNode(key[level])
                # print(key[level] + " inserted")
            current_node = current_node.children[index]
        # Mark the last character as leaf
        current_node.mark_as_leaf()
        # print("'" + key + "' inserted")

    def search(self, key):
        if key is None:
            return False
        key = key.lower()
        current_node = self.root
        index = 0

        for level in range(len(key)):
            index = self.get_index(key[level])
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]

        if not current_node and current_node.is_end_word:
            return True

        return False

    def top_k_suggestions(self, key, k):
        suggestions = []
        if not key or k == 0:
            return suggestions
        key = key.lower()
        current_node = self.root
        index = self.get_index(key)
        if not current_node.children[index]:
            return suggestions
        current_node = current_node.children[index]
        result = [key + word for word in self.find_words(current_node)]
        heapify(result)
        for num_word in range(k):
            suggestions.append(heappop(result))
            if not result:
                break
        return suggestions


    def delete(self):
        pass

    def get_words(self, root, result, level, word):
        # Leaf denotes end of a word
        if root.is_end_word:
            # current word is stored till the 'level' in the character array
            temp = ""
            for x in range(level):
                temp += word[x]
            result.append(str(temp))

        for i in range(26):
            if root.children[i]:
                # Non-None child, so add that index to the character array
                word[level] = chr(i + ord('a'))
                self.get_words(root.children[i], result, level + 1, word)

    def find_words(self, root):
        result = []
        word = [None] * 20
        self.get_words(root, result, 0, word)
        return result


def all_suggestions(trie: Trie, search_word, index, suggestions=None):
    if not suggestions:
        suggestions = []
    if index < len(search_word):
        suggestions = trie.top_k_suggestions(search_word[:index], 3)
    else:
        return suggestions
    return suggestions + all_suggestions(trie, search_word, index + 1)


if __name__ == '__main__':
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = 'mouse'
    trie = Trie()
    for product in products:
        trie.insert(product)
    print(all_suggestions(trie, search_word, 1))