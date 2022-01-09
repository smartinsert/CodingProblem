

def generate_subsets(arr: []):
    if not arr:
        return [[]]
    element = generate_subsets(arr[1:])
    return element + [[arr[0]] + y for y in element]


# TC: O(N*2^N)
# SC: O(N*2^N)
def generate_subsets_bfs(arr: []):
    if not arr:
        return [[]]
    subsets = []
    subsets.append([])
    for number in arr:
        current_subsets = len(subsets)
        for i in range(current_subsets):
            current_set = list(subsets[i])
            current_set.append(number)
            subsets.append(current_set)
    return subsets


# print(generate_subsets([1, 2, 3, 4]))
# print(generate_subsets_bfs([1, 2, 3, 4]))
print(generate_subsets_bfs([1, 3, 3]))




