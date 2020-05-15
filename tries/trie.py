from tries.trie_node import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def get_index(t):
        return ord(t) - ord('a')

    def insert(self, key):
        if key is None:
            return
        key = key.lower()
        current_node = self.root
        for level in range(len(key)):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[level])
                print(key[level] + " inserted")

            current_node = current_node.children[index]
        current_node.mark_as_leaf()
        print("'" + key + "' inserted")

    def search(self, key):
        if key is None:
            return False
        key = key.lower()
        current_node = self.root
        for level in range(len(key)):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]
        if current_node is not None and current_node.is_end_word:
            return True
        return False

if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]
    t = Trie()
    for key in keys:
        t.insert(key)