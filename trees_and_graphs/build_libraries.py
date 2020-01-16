class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_lst = [[] for _ in range(vertices)]

    def dfs(self, temp, vertex, visited):
        visited[vertex] = True
        temp.append(vertex)
        for i in self.adj_lst[vertex]:
            if not visited[i]:
                temp = self.dfs(temp, i, visited)
        return temp

    def add_edge(self, a, b):
        self.adj_lst[a].append(b)
        self.adj_lst[b].append(a)

    def connected_component(self):
        visited = []
        cc = []
        for i in range(self.vertices):
            visited.append(False)
        for vertex in range(self.vertices):
            if not visited[vertex]:
                temp = []
                cc.append(self.dfs(temp, vertex, visited))
        return cc


def compute_cost(n, c_lib, c_road, cities):
    g = Graph(n)
    for city in cities:
        g.add_edge(city[0] - 1, city[1] - 1)
    cc = g.connected_component()
    total_cost = 0
    for i in cc:
        num_roads = len(i) - 1
        total_library_cost = c_lib
        total_road_cost = num_roads * c_road
        total_cost += total_library_cost + total_road_cost
    return min(total_cost, n*c_lib)


if __name__ == '__main__':
    assert compute_cost(6, 2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]) == 12
