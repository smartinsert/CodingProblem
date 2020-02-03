"""
Max Heap implementation in python
"""


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self.__percolate_up(len(self.heap) - 1)

    def get_max(self):
        if self.heap:
            return self.heap[0]

    def remove_max(self):
        if len(self.heap) > 1:
            maximum = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__max_heapify(0)
            return maximum
        elif len(self.heap) == 1:
            maximum = self.heap[0]
            del self.heap[0]
            return maximum
        else:
            return None

    def __percolate_up(self, index):
        # left children of parent at k is located at 2k+1
        # parent =
        pass

    def __max_heapify(self, index):
        pass