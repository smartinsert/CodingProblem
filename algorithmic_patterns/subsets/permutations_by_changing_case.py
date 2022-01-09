"""
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""


# TC: O(N*2^N)
# SC: O(N*2^N)
def permutations_by_changing_case(input: str) -> [[]]:
    if not input:
        return []
    permutations = []
    permutations.append(input)

    for i in range((len(input))):
        current_permutations = len(permutations)
        for j in range(current_permutations):
            current_permutation = permutations[j]
            if current_permutation[i].isalpha():
                current_permutation = current_permutation[:i] + current_permutation[i].upper() + current_permutation[
                                                                                                 i + 1:]
                permutations.append(current_permutation)
    return permutations


print(permutations_by_changing_case('ad52'))
print(permutations_by_changing_case('ab7c'))
