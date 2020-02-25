"""
Given two binary trees with head reference as T and S having at most N TreeNodes. The task is to check if S is present as subtree in T.
A subtree of a tree T1 is a tree T2 consisting of a TreeNode in T1 and all of its descendants in T1.
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_if_subtree(S: TreeNode, T: TreeNode):
    """
    :param S: TreeTreeNode
    :param T: TreeTreeNode
    :return: true if S is a subtree of T
    """
    if not S and not T:
        return True
    if not S or not T:
        return False
    return S.data == T.data and check_if_subtree(S.left, T.left) and check_if_subtree(S.right, T.right)


def is_subtree(S: TreeNode, T: TreeNode):
    if not S:
        return True
    if not T:
        return False
    if check_if_subtree(S, T):
        return True
    return is_subtree(S, T.left) or is_subtree(S, T.right)


if __name__ == '__main__':
    T = TreeNode(26)
    T.right = TreeNode(3)
    T.right.right = TreeNode(3)
    T.left = TreeNode(10)
    T.left.left = TreeNode(4)
    T.left.left.right = TreeNode(30)
    T.left.right = TreeNode(6)

    """ TREE 2 
         Construct the following tree 
              10 
            /    \ 
          4      6 
           \ 
            30 
        """
    S = TreeNode(10)
    S.right = TreeNode(6)
    S.left = TreeNode(4)
    S.left.right = TreeNode(30)
    print(is_subtree(S, T))


