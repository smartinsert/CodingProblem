from heapq import *


class KthLargest:
    def __init__(self, initial, k):
        self.initial = initial
        self.k = k
        self.min_heap = []
        for number in initial:
            self.add(number)

    # Time: O(logK); Space: O(K)
    def add(self, number):
        heappush(self.min_heap, number)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]


if __name__ == '__main__':
    k_largest = KthLargest([3, 1, 5, 12, 2, 11], 4)
    print(k_largest.add(6))
