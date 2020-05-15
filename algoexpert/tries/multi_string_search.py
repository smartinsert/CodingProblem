class Trie:
    def __init__(self, string):
        self.root = {}
        self.__construct_trie(string)

    # Time: O(b^2); Space: O(b^2)
    def __construct_trie(self, string):
        for i in range(len(string)):
            self.__insert_substring_starting_at(i, string)

    def __insert_substring_starting_at(self, current_index, string):
        node = self.root
        for j in range(current_index, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    # Time: O(m); Space: O(1)
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True


def multiStringSearch(bigString, smallStrings):
    result = [False] * len(smallStrings)
    if not smallStrings or not bigString:
        return result
    trie = Trie(bigString)
    for idx, string in enumerate(smallStrings):
        if trie.contains(string):
            result[idx] = True
        else:
            result[idx] = False
    return result


def multi_string_search(big_string, small_strings):
    return [is_in_big_string(big_string, small_string) for small_string in small_strings]


def is_in_big_string(big_string, small_string):
    for i in range(len(big_string)):
        if i + len(small_string) > len(big_string):
            break
        if is_in_big_string_helper(big_string, small_string, i):
            return True
    return False


def is_in_big_string_helper(big_string, small_string, current_index):
    left_big_idx = current_index
    right_big_idx = current_index + len(small_string) - 1
    left_small_idx = 0
    right_small_idx = len(small_string) - 1
    while left_big_idx <= right_big_idx:
        if big_string[left_big_idx] != small_string[left_small_idx] or \
                small_string[right_small_idx] != big_string[right_big_idx]:
            return False
        left_small_idx += 1
        right_small_idx -= 1
        left_big_idx += 1
        left_small_idx -= 1
    return True


# class ModifiedTrie:
#     def __init__(self):
#         self.root = {}
#         self.end_symbol = '*'
#
#     def insert(self, string):
#         current_node = self.root
#         for i in range(len(string)):

if __name__ == '__main__':
    print(multiStringSearch('this is a big string', ['this', 'yo', 'is', 'a', 'bigger', 'string', 'kappa']))