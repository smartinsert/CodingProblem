"""
List of ratio given and need give the answer to m queries
Example :Given list [ a:b = 3, c:d = 4, g:h = 10, b:c = 8 ]
Query 1: What will be the a:d

equations = [["a", "b"], ["c", "d"], ["g", "h"], ["b", "c"]]
values = [3.0, 4.0, 10.0, 8.0],
queries = [ ["a", "d"]].
"""
from typing import List
from collections import defaultdict


def evaluate_ratios(equations: List[List[str]], values: List[float], queries: List[List[str]]):
    graph = defaultdict(list)
    results = []
    # Build graph
    for idx, equation in enumerate(equations):
        node_1 = equation[0]
        node_2 = equation[1]
        graph[node_1].append((node_2, values[idx]))
        graph[node_2].append((node_1, 1/values[idx]))

    for query in queries:
        if query[0] not in graph or query[1] not in graph:
            return results.append(-1)
        queue, visited = list(), list()
        queue.append((query[0], 1))
        while queue:
            node, current_product = queue.pop(0)
            if node == query[1]:
                results.append(current_product)
            visited.append(node)
            for neighbour, value in graph[node]:
                if neighbour not in visited:
                    queue.append((neighbour, current_product*value))
    return results


if __name__ == '__main__':
    print(evaluate_ratios(equations=[["a", "b"], ["c", "d"], ["g", "h"], ["b", "c"]],
                          values=[3.0, 4.0, 10.0, 8.0],
                          queries=[["a", "d"], ["b", "d"]]))