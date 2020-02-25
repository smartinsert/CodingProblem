"""
There are a total of A courses you have to take, labeled from 1 to A.

Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.
"""


def is_possible(number_of_courses, prerequisites):
    if len(prerequisites) <= 0:
        return True
    if number_of_courses == 0:
        return False

    sources, sorted_order = [], []
    graph = {k: [] for k in range(number_of_courses)}
    in_degrees = {k: 0 for k in range(number_of_courses)}

    # Build graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)
        in_degrees[child] += 1

    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            sources.append(vertex)

    while sources:
        current_vertex = sources.pop(0)
        sorted_order.append(current_vertex)
        for child in graph[current_vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)
    return len(sorted_order) == number_of_courses


if __name__ == '__main__':
    print(is_possible(3, [[0, 1], [1, 2]]))
