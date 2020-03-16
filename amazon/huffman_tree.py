"""
Huffman coding is a method of encoding characters based on their frequency.
Each letter is assigned a variable-length binary string, such as 0101 or 111110,
where shorter lengths correspond to more common letters. To accomplish this,
a binary tree is built such that the path from the root to any leaf uniquely maps to a character.
When traversing the path, descending to a left child corresponds to a 0 in the prefix, while descending right
corresponds to 1.
"""
from typing import List


class TreeNode:
    def __init__(self, character, count):
        self.character = character
        self.count = count
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.character}=>[count={self.count}, left={self.left}, right={self.right}]'


def build_tree(words: List[str]) -> TreeNode:
    character_to_frequency = {}
    for word in words:
        for character in word:
            character_to_frequency[character] = character_to_frequency.get(character, 0) + 1

    nodes = list()
    # Construct Tree Nodes
    for character in character_to_frequency.keys():
        node = TreeNode(character, character_to_frequency[character])
        nodes.append(node)

    # Sort nodes based on frequency
    nodes.sort(key=lambda n: n.count)

    if not nodes:
        return TreeNode(None, 0)

    return construct_tree_with(nodes)


def construct_tree_with(nodes: List[TreeNode]) -> TreeNode:
    # Handle single node
    if len(nodes) == 1:
        parent = nodes.pop(0)
        return parent

    left_node = nodes.pop(0)
    right_node = nodes.pop(0)

    # Encoding based on frequency of characters
    parent = TreeNode(None, left_node.count + right_node.count)
    parent.left = left_node
    parent.right = right_node

    nodes.append(parent)
    return construct_tree_with(nodes)


def map_characters_to_encoded_binary_strings(htree: TreeNode, character_map, huffman_code=""):
    if htree. character:
        character_map[htree.character] = huffman_code
        return
    # recurse for left subtree and assign zero value to hcode
    map_characters_to_encoded_binary_strings(htree.left, character_map, huffman_code + '0')
    # recurse for right subtree and assign one value to hcode
    map_characters_to_encoded_binary_strings(htree.right, character_map, huffman_code + '1')


if __name__ == '__main__':
    words = ['cats', 'cars', 'dogs']
    htree = build_tree(words)
    character_map = {}
    map_characters_to_encoded_binary_strings(htree, character_map)
    print(character_map)