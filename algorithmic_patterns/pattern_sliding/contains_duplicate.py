
def containsNearbyDuplicate(nums: [], k: int) -> bool:
    if not k or not nums:
        return False

    num_to_last_occurrence = {}

    for idx, number in enumerate(nums):
        if idx - num_to_last_occurrence.get(number, -float('inf')) <= k:
            return True
        num_to_last_occurrence[number] = idx
    return False


print(containsNearbyDuplicate([0, 1, 2, 3, 2, 5], 3))
print(containsNearbyDuplicate([1, 2, 3, 1], 3))
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
print(containsNearbyDuplicate([1, 2], 2))
