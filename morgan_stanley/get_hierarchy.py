"""
There are some employee manager relationship and based on input string , we have to print complete hierarchy.
For e.g.
Ajay-> Ramesh
Deepesh-> Animesh
Mohan->Ajay
Rahul-> Mohan

Input: Rahul
Output: Rahul->Mohan->Ajay->Ramesh
"""

from typing import List
from collections import defaultdict


def build_sorted_hierarchies(hierarchies: List[List[str]]) -> List:
    graph = defaultdict(list)
    in_degrees = dict()
    sources, sorted_hierarchy = list(), list()

    # build graph
    for hierarchy in hierarchies:
        parent = hierarchy[1]
        child = hierarchy[0]
        graph[parent].append(child)
        if child not in in_degrees:
            in_degrees[child] = 0
            if parent == 'X':
                continue
        in_degrees[child] += 1

    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            sources.append(vertex)

    while sources:
        current_vertex = sources.pop(0)
        sorted_hierarchy.append(current_vertex)
        for child in graph[current_vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)
    return sorted_hierarchy


def get_relationship_of(employee: str, hierarchies: List[List[str]]) -> List[str]:
    sorted_hierarchy = build_sorted_hierarchies(hierarchies)
    for idx, name in enumerate(sorted_hierarchy):
        if name == employee:
            return sorted_hierarchy[idx::-1]
    return []


if __name__ == '__main__':
    print(get_relationship_of('Rahul', [['Ajay', 'Ramesh'], ['Deepesh', 'Animesh'],
                                        ['Mohan', 'Ajay'], ['Rahul', 'Mohan'], ['Ramesh', 'X']]))
