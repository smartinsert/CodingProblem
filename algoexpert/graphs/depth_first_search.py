"""
Perform a DFS
Time: O(V+E)
Space: O(V)
"""


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, name):
        child = Node(name)
        self.children.append(child)
        return self

    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_seach(array)
        return array

