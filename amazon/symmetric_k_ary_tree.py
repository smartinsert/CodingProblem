"""
A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        return '{} -> {}'.format(self.data, self.children)


def update_levels_dict(node: TreeNode, levels, level_num):
    if level_num not in levels:
        levels[level_num] = list()
    levels[level_num].append(node.data)
    for child in node.children:
        update_levels_dict(child, levels, level_num + 1)


def is_symmetric(node):
    levels = dict()
    update_levels_dict(node, levels, 0)

    for level in levels:
        arr = levels[level]
        if arr != arr[::-1]:
            return False
    return True


if __name__ == '__main__':
    a = TreeNode(4)
    b = TreeNode(3)
    c = TreeNode(9)
    d = TreeNode(5)
    e = TreeNode(3)
    f = TreeNode(9)

    b.children = [c]
    e.children = [f]
    a.children = [b, d, e]

    print(is_symmetric(a))