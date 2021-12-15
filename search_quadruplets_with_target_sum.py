def search_quadruplets(arr: [], target: int) -> [[]]:
    if len(arr) < 4:
        return [[]]
    result = []
    triplets = []
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            search_triplets(arr, i, target - arr[i-1], triplets)
            triplets.append(arr[i-1])
            result.append(triplets)
    return result


def search_triplets(arr, left, target_sum, triplets) -> []:
    right = len(arr) - 1
    for i in range(left + 1, right):
        if i > 0 and arr[i-1] == arr[i]:
            continue
        pairs = search_pair(arr, i+1, target_sum - arr[i])
        for pair in pairs:
            triplets.append(arr[i])
            triplets.extend(pair)


def search_pair(arr, left, target_sum):
    right = len(arr) - 1
    pairs = []
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            pairs.append([arr[left], arr[right]])







