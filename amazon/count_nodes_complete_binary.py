class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_nodes(node):
    pass


if __name__ == '__main__':
    n1 = TreeNode(10)
    n2 = TreeNode(5)
    n3 = TreeNode(3)
    n4 = TreeNode(2)
    n5 = TreeNode(1)
    n6 = TreeNode(15)
    n7 = TreeNode(20)
    n8 = TreeNode(25)
    n9 = TreeNode(7)
    n10 = TreeNode(6)
    n11 = TreeNode(9)
    n12 = TreeNode(17)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    n4.left, n4.right = n8, n9
    n5.left, n5.right = n10, n11
    n6.left = n12
