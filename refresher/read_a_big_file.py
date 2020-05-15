from heapq import *


def read_large_file(file_handler, block_size=10000):
    buffer = []
    for line in file_handler:
        buffer.append(line)
        if len(buffer) == block_size:
            yield buffer
            buffer = []
    if buffer:
        yield buffer


def sort_file(path):
    sorted_words = []
    with open(path) as file_handler:
        for block in read_large_file(file_handler):
            for word in block.split(' '):
                heappush(sorted_words, word)
    while sorted_words:
        print(heappop(sorted_words))
