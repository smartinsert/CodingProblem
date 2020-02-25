"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed
before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to
schedule all the tasks.

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
"""


def scheduling_order(tasks, prerequisites):
    task_order, sources = [], []
    if tasks <= 0:
        return task_order
    # Initialize graph
    graph = {k: [] for k in range(tasks)}
    # Initialize indegree hash map
    vertex_to_indegree = {k: 0 for k in range(tasks)}

    # Build graph
    for prerequisite in prerequisites:
        parent = prerequisite[0]
        child = prerequisite[1]
        graph[parent].append(child)
        vertex_to_indegree[child] += 1

    for vertex in vertex_to_indegree:
        if vertex_to_indegree[vertex] == 0:
            sources.append(vertex)

    while sources:
        current_vertex = sources.pop(0)
        task_order.append(current_vertex)
        # Traverse through the children of the current vertex and update the in depth
        for child in graph[current_vertex]:
            vertex_to_indegree[child] -= 1
            if vertex_to_indegree[child] == 0:
                sources.append(child)

    if len(task_order) != tasks:
        return False
    return True


if __name__ == '__main__':
    print(scheduling_order(tasks=3, prerequisites=[[0, 1], [1, 2]]))
    print(scheduling_order(tasks=3, prerequisites=[[0, 1], [1, 2], [2, 0]]))