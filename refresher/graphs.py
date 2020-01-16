graph = {
    0: {},
    1: {0},
    2: {0},
    3: {1, 2},
    4: {3}
}


def package_dependencies(dependencies):
    visited = set([])
    result = []

    def dfs(node):
        for next_node in dependencies[node]:
            if next_node not in visited:
                dfs(next_node)
        visited.add(node)
        result.append(node)

    for node in dependencies.keys():
        dfs(node)

    return result


if __name__ == '__main__':
    print(package_dependencies(graph))