"""
There's an undirected connected graph with n nodes labeled 1..n. But some of the edges has been broken disconnecting
the graph. Find the minimum cost to repair the edges so that all the nodes are once again accessible from each other.

Input:

n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes connected by an edge.
edgesToRepair, a list where each element is a triplet representing the pair of nodes between which an edge is
currently broken and the cost of repearing that edge, respectively (e.g. [1, 2, 12] means to repear an edge between
nodes 1 and 2, the cost would be 12).
"""
# Kruskal's algorithm

from collections import defaultdict
import heapq


class Solution:
    def __init__(self):
        pass

    def min_cost_of_repair(self, edges, edges_to_repair):
        graph = defaultdict(list)
        added_edges = set()
        for edge in edges_to_repair:
            graph[edge[0]].append((edge[2], edge[1]))
            graph[edge[1]].append((edge[2], edge[0]))
            added_edges.add((edge[0], edge[1]))
            added_edges.add((edge[1], edge[0]))
        for edge in edges:
            if tuple(edge) not in added_edges:
                graph[edge[0]].append((0, edge[1]))
                graph[edge[1]].append((0, edge[0]))

        res = 0
        queue = [(0, 1)]
        heapq.heapify(queue)
        visited = set()

        while queue:
            minCost, node = heapq.heappop(queue)
            if node not in visited:
                visited.add(node)
                res += minCost
                for cost, connectedNode in graph[node]:
                    if connectedNode not in visited:
                        heapq.heappush(queue, (cost, connectedNode))

        return res


s = Solution()

# print(s.min_cost_ofRepair([[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
# print(s.min_cost_ofRepair([[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]]))
# print(s.min_cost_ofRepair([[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
#                          [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))
print(s.min_cost_of_repair([[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))

