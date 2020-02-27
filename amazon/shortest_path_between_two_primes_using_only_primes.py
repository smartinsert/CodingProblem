"""
Given two four digit prime numbers, suppose 1033 and 8179,
we need to find the shortest path from 1033 to 8179 by altering only single digit at a time such that every number
that we get after changing a digit is prime.
"""

# Generate all four digit primes using sieve of erastosthenes
# Build a graph with vertices as the indices of the prime set generated above and connect an edge only if the two
# numbers differ by a single digit
# perform a bfs to find the shortest path


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, a: int, b: int):
        self.adjacency_list[b].append(a)
        self.adjacency_list[a].append(b)

    def bfs(self, source_idx, destination_idx):
        queue = []
        visited = [0 for _ in range(self.vertices)]
        visited[source_idx] = 1
        queue.append(source_idx)
        while queue:
            current_vertex = queue.pop(0)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if not visited[adjacent_vertex]:
                    visited[adjacent_vertex] = visited[current_vertex] + 1
                    queue.append(adjacent_vertex)
                elif adjacent_vertex == destination_idx:
                    return visited[adjacent_vertex] - 1


# Sieve of Erastosthenes
def generate_primes(number_of_digits):
    prime_set = []
    last_prime = 10**number_of_digits - 1
    primes = [True for _ in range(last_prime + 1)]
    current_prime = 2
    while current_prime * current_prime <= last_prime:
        if primes[current_prime]:
            # Mark all multiples of current prime to be False
            for i in range(current_prime * current_prime, last_prime + 1, current_prime):
                primes[i] = False
        current_prime += 1
    for i in range(10**(number_of_digits - 1), last_prime + 1):
        if primes[i]:
            prime_set.append(i)
    return prime_set


def compare_numbers(first, second):
    first_str = str(first)
    second_str = str(second)
    number_of_different_characters = 0
    if first_str[0] != second_str[0]:
        number_of_different_characters += 1
    if first_str[1] != second_str[1]:
        number_of_different_characters += 1
    if first_str[2] != second_str[2]:
        number_of_different_characters += 1
    if first_str[3] != second_str[3]:
        number_of_different_characters += 1
    return number_of_different_characters == 1


def shortest_path(source_number, target_number, prime_set):
    graph = Graph(len(prime_set))
    source_number_idx, destination_number_idx = None, None
    for i in range(len(prime_set)):
        for j in range(i + 1, len(prime_set)):
            if compare_numbers(prime_set[i], prime_set[j]):
                graph.add_edge(i, j)
    for i in range(len(prime_set)):
        if prime_set[i] == source_number:
            source_number_idx = i
    for i in range(len(prime_set)):
        if prime_set[i] == target_number:
            destination_number_idx = i
    return graph.bfs(source_number_idx, destination_number_idx)


if __name__ == '__main__':
    prime_set = generate_primes(4)
    print(shortest_path(source_number=1033, target_number=8179, prime_set=prime_set))
    print(shortest_path(source_number=1373, target_number=8017, prime_set=prime_set))




