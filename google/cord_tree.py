"""
A cord tree is a binary tree of strings.
A node in this tree can be a leaf node or an internal node.
An internal node has two children, a left child and a right child. It also has a length of all the children under it
A leaf nodes have a value and a length

                                #      InternalNode, 26
                                #      /              \
                                #     /                \
                                #    /                  \
                                # Leaf(5, ABCDE)      InternalNode, 21
                                #                       /           \
                                #                      /             \
                                #                     /               \
                                #                    /                 \
                                #         Leaf(10, FGHIJKLMNO)     Leaf(11, PQRSTUVWXYZ)
Q1: Define a Data Structure that represents a Cord tree.
Q2: Define a function that takes in a tree and an index and returns the character at that index.
"""

from collections import deque


class CordTree:
    def __init__(self, root):
        self.root = root


class InternalNode:
    def __init__(self, left, right, length):
        self.left = left
        self.right = right
        self.length = length


class LeafNode:
    def __init__(self, length, value):
        self.value = value
        self.length = length


def find_cord_at_index(tree, index):
    if not tree.root:
        return ""

    queue = deque([tree.root])

    current_index = 0

    while queue:
        node = queue.popleft()

        if isinstance(node, InternalNode):
            queue.append(node.left)
            queue.append(node.right)
            continue

        if (current_index + node.length) <= index:
            current_index += node.length
            continue

        index_to_return = index - current_index

        return node.value[index_to_return]

    return ""


def find_cord_at_index_opt(root, index):
    if not root or index < 0:
        return None
    elif isinstance(root, InternalNode):
        if not root.left:
            return find_cord_at_index_opt(root.right, index)
        elif not root.right:
            return find_cord_at_index_opt(root.left, index)
        else:
            left, right = root.left, root.right
            if index < left.length:
                search = left
            else:
                search = right
                index -= left.length
            return find_cord_at_index_opt(search, index)
    else:
        return root.value[index] if index < root.length else None


if __name__ == "__main__":
    root = InternalNode(LeafNode(5, "ABCDE"), InternalNode(LeafNode(10, "FGHIJKLMNO"), LeafNode(11, "PQRSTUVWXYZ"), 21),
                        26)

    # print(find_cord_at_index(CordTree(root), 7))
    print(find_cord_at_index_opt(root, 7))
