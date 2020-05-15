class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


#Time: O(h); where h is the height of the tree
def lowest_common_ancestor(node: TreeNode, p: TreeNode, q: TreeNode) -> int:
    if not node:
        return -1
    if node.left and p.data < node.data and q.data < node.data:
        return lowest_common_ancestor(node.left, p, q)
    elif node.right and p.data > node.data and q.data > node.data:
        return lowest_common_ancestor(node.right, p, q)
    else:
        return node.data


if __name__ == '__main__':
    n1 = TreeNode(6)
    n2 = TreeNode(2)
    n3 = TreeNode(8)
    n4 = TreeNode(0)
    n5 = TreeNode(4)
    n6 = TreeNode(7)
    n7 = TreeNode(9)
    n8 = TreeNode(3)
    n9 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n5.left = n8
    n5.right = n9
    n3.left = n6
    n3.right = n7.right
    print(lowest_common_ancestor(n1, n2, n5))