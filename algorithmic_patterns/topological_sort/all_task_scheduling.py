"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed
before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all
possible ordering of tasks meeting all prerequisites.
"""


# Time: O(V!*E); where V is the total number of tasks and E is the number of prerequisites
def all_possible_task_ordering(tasks, prerequisites):
    all_possible_orderings = []
    if tasks == 0:
        return all_possible_orderings
    sources = []
    graph, in_degrees = {}, {}
    for i in range(tasks):
        in_degrees[i] = 0
        graph[i] = []
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)
        in_degrees[child] += 1

    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            sources.append(vertex)
    all_possible_task_ordering_util(graph, in_degrees, sources, all_possible_orderings)


def all_possible_task_ordering_util(graph, in_degrees, sources, all_possible_orderings):
    if sources:
        for vertex in sources:
            all_possible_orderings.append(vertex)
            source_for_next_cycle = sources.copy()
            source_for_next_cycle.remove(vertex)
            for child in graph[vertex]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    source_for_next_cycle.append(child)
            all_possible_task_ordering_util(graph, in_degrees, source_for_next_cycle, all_possible_orderings)
            all_possible_orderings.remove(vertex)
            for child in graph[vertex]:
                in_degrees[child] += 1
    if len(all_possible_orderings) == len(in_degrees):
        print(all_possible_orderings)


if __name__ == '__main__':
    print(all_possible_task_ordering(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))
