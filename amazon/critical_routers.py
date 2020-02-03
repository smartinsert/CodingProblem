"""
You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which,
 when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of
 connected components in the graph). The task is to find all articulation points in the given graph.

Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
"""
import collections


def dfs(rank, node, prev_node, edges, low):
    low[node], result = rank, []
    child_count = 0
    for next_node in edges[node]:
        if next_node == prev_node: continue
        if not low[next_node]:
            child_count += 1
            result += dfs(rank+1, next_node, node, edges, low)
        low[node] = min(low[node], low[next_node])
        if prev_node != -1 and low[next_node] > rank:
            result.append(node)
        elif prev_node == -1 and child_count >= 2:
            result.append(node)
    return result


if __name__ == '__main__':
    n = 7
    connections = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

    low, edges = [0] * n, collections.defaultdict(list)

    for u, v in connections:
        edges[u].append(v)
        edges[v].append(u)

    results = dfs(1, 0, -1, edges, low)
    print(results)

