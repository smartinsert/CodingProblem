"""
You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which,
 when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of
 connected components in the graph). The task is to find all articulation points in the given graph.

Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices + 1
        self.adj_list = defaultdict(list)
        self.parent = [-1] * self.V
        self.low = [float('inf')] * self.V
        self.disc = [float('inf')] * self.V
        self.visited = [False] * self.V
        self.time = 0
        self.articulation_points = []

    def add_edge(self, v, u):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_articulation_point(self, u):
        # to keep track of which vertices are visited
        self.visited[u] = True
        # to check the lowest vertex that this node can reach through its children
        self.low[u] = self.time
        # the time that this vertex was discovered - useful to identify when a child vertex can reach its parents ancestors
        self.disc[u] = self.time
        # a way to record the when a vertex was first encountered
        self.time += 1

        # loop over each child vertex of u
        for v in self.adj_list[u]:

            # if the child vertex v has not been visited then enter here
            if not self.visited[v]:
                # mark the parent of v as u as it was first discovered by u
                self.parent[v] = u
                # depth first search over its children
                self.find_articulation_point(v)

                # once we complete the dfs and come back here
                # we update the lowest vertex that we can reach from any child of u
                self.low[u] = min(self.low[u], self.low[v])

                # if the lowest vertex of child v is greater [which means below] then when u was discovered,
                # then it is assumed that v does not have a way back to u
                # and therefore v and u are not in a cycle and hence a bridge
                if self.low[v] > self.disc[u]:
                    self.articulation_points.append(u)

# if v is already visited then we check if v is the parent of u, if yes then that means no need to update the lowest
                # vertex for u and v is above it.
                # else it means v is an ancestor of u and there is a back edge between u or subtree rooted at u back
                # to v and we need to find the earliest time that was used to visit u using the logic mentioend below.
            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.disc[v])


if __name__ == '__main__':
    n = 7
    connections = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

    g = Graph(n)
    for i in connections:
        g.add_edge(i[0], i[1])

    for j in range(1, g.V):
        if not g.visited[j]:
            g.find_articulation_point(j)

    print(g.articulation_points)
