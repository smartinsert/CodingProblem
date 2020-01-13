graph = {
    'A': {'B', 'C', 'F'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'A', 'C', 'E'}
}


def dfs_traversal(graph, start):
    visited, stack = list(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
        for next_node in graph[node]:
            if next_node not in visited:
                stack.append(next_node)
    return visited


def bfs_traversal(graph, start):
    visited, queue = list(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
        for next_node in graph[node]:
            if next_node not in visited:
                queue.append(next_node)
    return visited


if __name__ == '__main__':
    print(dfs_traversal(graph, 'A'))
    print(bfs_traversal(graph, 'A'))