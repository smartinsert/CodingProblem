"""
Given a tuple where the first element is the parent and the second element is the child. Check if it is a valid
binary tree
"""


'''
A tree is a valid binary tree iff
1. There is only one root
2. If each node has a single parent(1 indegree)
3. Each node has no more than 2 children
4. There is no cycle
'''


class Tree:
    def __init__(self, tuples):
        self.in_degrees = {}
        self.adj_list = {}
        self._build_tree(tuples)

    def _build_tree(self, tuples):
        for parent, child in tuples:
            if parent not in self.adj_list:
                self.adj_list[parent] = []
            if parent not in self.in_degrees:
                self.in_degrees[parent] = 0
            if child not in self.in_degrees:
                self.in_degrees[child] = 0
            self.adj_list[parent].append(child)
            self.in_degrees[child] += 1

    def has_one_root(self):
        root = [node for node, value in self.in_degrees.items() if value == 0]
        return len(root) == 1

    def has_two_children(self):
        for node in self.adj_list:
            children = self.adj_list[node]
            if len(children) > 2:
                return False
        return True

    def has_one_parent(self):
        for node in self.in_degrees:
            if self.in_degrees[node] > 1:
                return False
        return True

    def has_a_cycle(self):
        sources = [node for node, value in self.in_degrees.items() if value == 0]
        top_sort = []
        while sources:
            current_source = sources.pop()
            top_sort.append(current_source)
            for child in self.adj_list[current_source]:
                self.in_degrees[child] -= 1
                if self.in_degrees[child] == 0:
                    sources.append(child)
        return len(top_sort) == len(self.in_degrees)

    def is_valid(self):
        return self.has_one_root() and self.has_two_children() and self.has_one_parent() and not self.has_a_cycle()


if __name__ == '__main__':
    tree = Tree([(1, 2), (2, 3), (3, 4)])
    print(tree.is_valid())