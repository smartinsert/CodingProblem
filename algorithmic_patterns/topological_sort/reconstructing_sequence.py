"""
Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely
reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the
array are subsequences of it.

Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
Output: true
"""


def is_reconstruction_possible(original_sequence, sequences):
    if len(original_sequence) == 0:
        return False

    if len(sequences) == 0:
        return False

    in_degrees = {}
    graph = {}

    sources, sorted_order = [], []

    for sequence in sequences:
        for number in sequence:
            in_degrees[number] = 0
            graph[number] = []

    # Not enough numbers to construct the sequence
    if len(in_degrees) != len(original_sequence):
        return False

    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i-1], sequence[i]
            graph[parent].append(child)
            in_degrees[child] += 1

    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            sources.append(vertex)

    # Perform BFS
    while sources:
        # If there are more than one source
        if len(sources) > 1:
            return False

        # If the current number in the original sequence does not follow the same order as sources
        if original_sequence[len(sorted_order)] != sources[0]:
            return False

        vertex = sources.pop(0)
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)

    return len(sorted_order) == len(original_sequence)


if __name__ == '__main__':
    print(is_reconstruction_possible([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]]))
