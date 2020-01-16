class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_lst = [[] for _ in range(vertices)]

    def add_edge(self, a, b):
        self.adj_lst[a].append(b)
        self.adj_lst[b].append(a)

    def cost_to_travel_from(self, source, condition):
        visited, queue = set(), [(source, 0)]
        visited.add(source)
        while queue:
            node, distance = queue.pop()
            for neighbour in self.adj_lst[node]:
                if condition(neighbour):
                    return distance + 1
                visited.add(neighbour)
                queue.append((neighbour, distance+1))
        return -1


def shortest_path(g_nodes: int, g_from: list, g_to: list, ids: list, val: int):
    if not g_nodes:
        return -1
    color_to_match = ids[val - 1]
    components = list(zip(g_from, g_to))
    graph = Graph(g_nodes)
    for component in components:
        graph.add_edge(component[0]-1, component[1]-1)
    return graph.cost_to_travel_from(val, lambda node: ids[node - 1] == color_to_match)


if __name__ == '__main__':
    print(shortest_path(5, [1, 2, 2, 3], [2, 3, 4, 5], [1, 2, 3, 1, 3], 1))
    print(shortest_path(5, [1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2))
