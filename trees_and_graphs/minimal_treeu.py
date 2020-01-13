class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        string = '(' + str(self.value)
        if self.left:
            string += str(self.left)
        else:
            string += '.'
        if self.right:
            string += str(self.right)
        else:
            string += '.'
        return string + ')'


def minimal_height_tree(sorted_array):
    if len(sorted_array) == 0:
        return None
    if len(sorted_array) == 1:
        return BSTNode(sorted_array[0])
    mid = len(sorted_array)//2
    left = minimal_height_tree(sorted_array[:mid])
    right = minimal_height_tree(sorted_array[mid+1:])
    return BSTNode(sorted_array[mid], left, right)