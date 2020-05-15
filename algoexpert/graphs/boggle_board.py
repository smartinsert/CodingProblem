"""
Find all the words in a boggle board, DFS and Trie
Time Complexity: w*s(Trie Construction) + n*m*8^s(matrix exploration) where s is the length of the longest word in
the search list and w is the number of words.
Space Complexity: w*s(Trie) + n*m(visited matrix) + s(recursion stack) + w(result list) = w*s + n*m
"""


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = word

    def contains(self, word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return True


def get_neighbors(i, j, board):
    neighbours = []
    if i > 0 and j > 0:
        neighbours.append([i-1, j-1])
    if i > 0 and j < len(board[0]) - 1:
        neighbours.append([i-1, j+1])
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbours.append([i+1, j+1])
    if i < len(board) - 1 and j > 0:
        neighbours.append([i+1, j-1])
    if i > 0:
        neighbours.append([i-1, j])
    if i < len(board) - 1:
        neighbours.append([i+1, j])
    if j > 0:
        neighbours.append([i, j-1])
    if j < len(board[0]) - 1:
        neighbours.append([i, j+1])
    return neighbours


def boggle_board(board, words):
    rows = len(board)
    columns = len(board[0])
    if not rows and not columns:
        return []
    final_words = set()
    trie = Trie()
    for word in words:
        trie.add(word)
    visited = [[False for letter in row] for row in board]
    for i in range(rows):
        for j in range(columns):
            explore(i, j, board, trie.root, visited, final_words)
    return final_words


def explore(i, j, board, trie_node, visited, final_words):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trie_node:
        return
    visited[i][j] = True
    trie_node = trie_node[letter]
    if '*' in trie_node:
        final_words.add(trie_node['*'])
    neighbours = get_neighbors(i, j, board)
    for neighbour in neighbours:
        explore(neighbour[0], neighbour[1], board, trie_node, visited, final_words)
    visited[i][j] = False
