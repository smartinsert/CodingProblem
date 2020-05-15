"""
Get youngest common ancestor of two descendants
"""


# Time: O(D); Space: O(1)
def get_youngest_ancestor(top_ancestor, descendant_one, descendant_two):
    depth_one = get_depth_from(top_ancestor, descendant_one)
    depth_two = get_depth_from(top_ancestor, descendant_two)

    if depth_one > depth_two:
        return backtrack_ancestral_tree(descendant_two, descendant_one, depth_one - depth_two)
    else:
        return backtrack_ancestral_tree(descendant_one, descendant_two, depth_two - depth_one)


def get_depth_from(ancestor, descendant):
    depth = 0
    while descendant != ancestor:
        descendant = descendant.ancestor
        depth +=1
    return depth


def backtrack_ancestral_tree(lower_descendant, higher_descendant, difference):
    while difference > 0:
        lower_descendant = lower_descendant.ancestor
        difference -= 1
    while higher_descendant != lower_descendant:
        higher_descendant = higher_descendant.ancestor
        lower_descendant = lower_descendant.ancestor
    return lower_descendant