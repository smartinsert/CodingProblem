import math
import os
import random
import re
import sys


def mean(ar, n):
    return round(sum(ar) / n, 2)


def median(ar, n):
    ar = sorted(ar)
    if not n % 2:
        return mean(ar[(n // 2) - 1:(n // 2) + 1], 2)
    return ar[n // 2]


def mode(ar, n):
    ar = sorted(ar)
    count_ar = [0] * (ar[-1] + 1)
    for i in ar:
        count_ar[i] += 1
    return count_ar.index(max(count_ar))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # ar = list(map(int, input().rstrip().split()))

    # result = mean([64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060], 10)

    # fptr.write(str(result) + '\n')
    #
    # result = median([64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060], 10)
    #
    # fptr.write(str(result) + '\n')
    #
    print(mode([1, 5, 4, 7, 7, 7], 4))
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
