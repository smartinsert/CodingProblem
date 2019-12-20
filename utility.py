# Flatten out list of tuples to list
l = []
flattened = [item for sublist in l for item in sublist]

# Frequency of items in a list of list

from collections import Counter
from itertools import chain
test_list = []
res = dict(Counter(chain.from_iterable(map(set, test_list))))

# Frequency of items in a list of list
number_to_freq = dict()
flattened_intervals = []
for items in flattened_intervals:
    number_to_freq[items] = flattened_intervals.count(items)