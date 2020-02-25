"""
Given a directed graph, find the topological ordering of its vertices.
Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0
"""


def topological_ordering(vertices, edges):
    if not vertices:
        return []
    topological_order, sources = [], []

    in_degrees = {k: 0 for k in range(vertices)}
    graph = {k: [] for k in range(vertices)}
    # Build graph
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        graph[parent].append(child)
        in_degrees[child] += 1

    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            sources.append(vertex)

    # Traverse the graph and keep adding the source till the sink is reached
    while sources:
        parent = sources.pop(0)
        topological_order.append(parent)
        for child in graph[parent]:
            in_degrees[child] -=1
            if in_degrees[child] == 0:
                sources.append(child)

    # check if there is a cycle
    if len(topological_order) != vertices:
        return []
    return topological_order


if __name__ == '__main__':
    print(topological_ordering(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))



