"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.
"""

from typing import List


def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    result = [[]] * len(people)
    people.sort(key=lambda x: (x[0], -x[1]))
    indices = [i for i in range(len(people))]
    for j, (_, pk) in enumerate(people):
        i = indices.pop(pk)
        result[i] = people[j]
    return result


if __name__ == '__main__':
    print(reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))