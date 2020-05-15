"""
Perform a BFS
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

    def breadth_first_search(self, array):
        if not array:
            return []

        queue = [self]

        while queue:
            current_node = queue.pop(0)
            array.append(current_node.name)
            for child in current_node.children:
                queue.append(child)
        return array