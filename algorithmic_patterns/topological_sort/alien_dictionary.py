"""
There is a dictionary containing words from an alien language for which we don’t know the ordering of the characters.
Write a method to find the correct order of characters in the alien language.

Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac

Explanation:
Each word in the word list specify some ordering. In the above example, a comes after b, c comes after b,
c comes after a; then by the principle of transitivity, the order is b > a > c

Construct the edges of the graph based on the rules laid down by the words then apply topological sort
"""


def correct_ordering(words):
    order, sources = [], []
    in_degrees, graph = {}, {}
    for word in words:
        for character in word:
            in_degrees[character] = 0
            graph[character] = []

    for i in range(0, len(words) - 1):
        first_word = words[i]
        second_word = words[i+1]
        for j in range(0, min(len(first_word), len(second_word))):
            parent, child = first_word[j], second_word[j]
            if parent != child:
                graph[parent].append(child)
                in_degrees[child] += 1
                break

    for vertex in in_degrees:
        if in_degrees[vertex] == 0:
            sources.append(vertex)

    while sources:
        current_vertex = sources.pop(0)
        order.append(current_vertex)
        for child in graph[current_vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)

    if len(order) != len(in_degrees):
        return ''
    return ''.join(order)


if __name__ == '__main__':
    print(correct_ordering(["ba", "bc", "ac", "cab"]))
    print(correct_ordering(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))



