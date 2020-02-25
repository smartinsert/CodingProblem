"""
Write a method to find all MHTs of the given graph and return a list of their roots.
All the trees without leaf nodes are candidates for MHTs. Prune all nodes, till we have tree with just one or two
nodes, that will give us the MHTs. We will make leaves as our sources and prune them till we have one or two nodes
"""


def find_all_minimum_height_tree_vertices(num_vertices, edges):
    if num_vertices <= 0:
        return []

    if num_vertices == 1:
        return [0]

    graph, in_degrees, leaves = {}, {}, []

    for i in range(num_vertices):
        in_degrees[i] = 0
        graph[i] = []

    for edge in edges:
        parent, child = edge[0], edge[1]
        # since this is an undirected graph
        graph[parent].append(child)
        graph[child].append(parent)
        in_degrees[child] += 1
        in_degrees[parent] += 1

    for vertex in in_degrees:
        # add leaf to the leaves
        if in_degrees[vertex] == 1:
            leaves.append(vertex)

    number_of_nodes = num_vertices
    while number_of_nodes > 2:
        leaves_size = len(leaves)
        number_of_nodes -= leaves_size
        for i in range(leaves_size):
            vertex = leaves.pop(0)
            for child in graph[vertex]:
                in_degrees[child] -= 1
                if in_degrees[child] == 1:
                    leaves.append(child)
    return list(leaves)


if __name__ == '__main__':
    print(find_all_minimum_height_tree_vertices(5, [[0, 1], [1, 2], [1, 3], [2, 4]]))
