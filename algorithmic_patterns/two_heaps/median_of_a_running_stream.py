"""
Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
"""
from heapq import *


class Median:
    def __init__(self):
        self.small_numbers_list = []
        self.large_number_list = []
        self._median = 0.

    def insert_number(self, number):
        if not self.large_number_list or -self.large_number_list[0] >= number:
            heappush(self.large_number_list, -number)
        else:
            heappush(self.small_numbers_list, number)
        if len(self.large_number_list) > len(self.small_numbers_list) + 1:
            heappush(self.small_numbers_list, -heappop(self.large_number_list))
        elif len(self.large_number_list) < len(self.small_numbers_list):
            heappush(self.large_number_list, -heappop(self.small_numbers_list))

    def find_median(self):
        if not self.large_number_list and not self.small_numbers_list:
            return 0
        if len(self.large_number_list) == len(self.small_numbers_list):
            return -self.large_number_list[0] / 2.0 + self.small_numbers_list[0] / 2.0
        else:
            return -self.large_number_list[0]


if __name__ == '__main__':
    median = Median()
    print(median.find_median())

    median.insert_number(5)
    median.insert_number(10)
    median.insert_number(1)

    print(median.find_median())