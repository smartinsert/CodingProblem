class Node:
    def __init__(self, data, adjacency_list=None):
        self.data = data
        self.adjacency_list = adjacency_list or list()
        self.shortest_path = None

    def add_edge_to(self, node):
        self.adjacency_list += [node]

    def __str__(self):
        return self.data


class Queue:
    def __init__(self):
        self.values = list()

    def add(self, value):
        self.values.append(value)

    def remove(self):
        if self.values:
            value = self.values[0]
            del self.values[0]
            return value
        return None

    def is_empty(self):
        return not len(self.values)


def str_for(path):
    if not path:
        return str(path)
    return ''.join([str(n) for n in path])


def find_route(source, destination):
    queue = Queue()
    path_found = None
    node = source
    node.shortest_path = [node]
    all_visited_nodes = [node]
    while node:
        for adjacent in node.adjacency_list:
            adjacent.shortest_path = node.shortest_path + [adjacent]
            if adjacent == destination:
                path_found = node.shortest_path + [adjacent]
                break
            queue.add(adjacent)
            all_visited_nodes.append(adjacent)
        node = queue.remove()
    for visited in all_visited_nodes:
        visited.shortest_path = None
    return path_found


if __name__ == '__main__':
    node_j = Node('J')
    node_i = Node('I')
    node_h = Node('H')
    node_d = Node('D')
    node_f = Node('F', [node_i])
    node_b = Node('B', [node_j])
    node_g = Node('G', [node_d, node_h])
    node_c = Node('C', [node_g])
    node_a = Node('A', [node_b, node_c, node_d])
    node_e = Node('E', [node_f, node_a])
    node_d.add_edge_to(node_a)
    assert str_for(find_route(node_a, node_i)) == 'None'