"""
There are N cities numbered from 1 to N.
You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and
city2together. (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)
Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1)
that connects those two cities together. The cost is the sum of the connection costs used.
 If the task is impossible, return -1.
"""


def minimum_cost(connections, num_islands):
    sorted_connections = sorted(connections, key=lambda x: x[2])
    parent_set = [i for i in range(1, num_islands+1)]
    cost, visited = 0, 1
    for connection in sorted_connections:
        x = find(connection[0], parent_set)
        y = find(connection[1], parent_set)
        if x != y:
            parent_set[x-1] = y
            visited += 1
            cost += connection[2]
            if visited == num_islands:
                return cost
    return -1


def find(vertex, parent_set):
    if parent_set[vertex-1] != vertex:
        parent_set[vertex-1] = find(parent_set[vertex-1], parent_set)
    return parent_set[vertex-1]


if __name__ == '__main__':
    A = 4
    B = [[1, 2, 1],
         [2, 3, 4],
         [1, 4, 3],
         [4, 3, 2],
         [1, 3, 10]]
    print(minimum_cost(B, A))