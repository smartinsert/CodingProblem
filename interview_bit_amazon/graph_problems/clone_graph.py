"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
"""

from typing import List


class Node:
    def __init(self, value: int, neighbours: List):
        self.value = value
        self.neighbours = neighbours

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)


def clone_graph(node: Node):
    visited = {}
    return clone_graph_util(node, visited)


def clone_graph_util(node: Node, visited):
    if not node:
        return None

    # Return the already cloned copy
    if node in visited:
        return visited[node]

    # Else create a clone of the node and all its neighbours
    cloned_node = Node(node.value, [])
    visited[node] = cloned_node

    for neighbour in node.neighbours:
        cloned_node.neighbours.append(clone_graph_util(neighbour, visited))

    return cloned_node
