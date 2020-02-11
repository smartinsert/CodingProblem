class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data: int):
        if not self.head:
            self.head = Node(data)
            return
        else:
            new_node = Node(data)
            new_node.next_element = self.head
            self.head = new_node

    def append(self, data: int):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next_element:
                current = current.next_element
            current.next_element = Node(data)


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [LinkedList() for _ in range(self.vertices)]

    def add_edge(self, source: int, destination: int):
        self.adjacency_list[source].insert_at_head(destination)


class brea
