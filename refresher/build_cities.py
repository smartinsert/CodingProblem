class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_lst = [[] for _ in range(vertices)]

    def add_edge(self, a, b):
        self.adj_lst[a].append(b)
        self.adj_lst[b].append(a)

    def dfs_util(self, result, v, visited):
        visited[v] = True
        result.append(v)
        for i in self.adj_lst[v]:
            if i not in visited:
                result = self.dfs_util(result, i, visited)
        return result

    def connected_component(self):
        visited = []
        cc = []
        for i in range(self.vertices):
            visited.append(False)
        for v in range(self.vertices):
            if not visited[v]:
                result = []
                cc.append(self.dfs_util(result, v, visited))
        return cc


if __name__ == '__main__':
    graph = Graph(3)
    graph.add_edge(0, 1)
    graph.add_edge(2, 0)
    graph.add_edge(1, 2)
    print(graph.connected_component())
