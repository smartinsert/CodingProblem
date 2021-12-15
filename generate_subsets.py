

def generate_subsets(arr: []):
    if not arr:
        return [[]]
    element = generate_subsets(arr[1:])
    return element + [[arr[0]] + y for y in element]


# print(generate_subsets([1, 2, 3, 4]))




