"""
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
"""

from collections import defaultdict
from bisect import bisect


class TimeMap:
    def __init__(self):
        self.key_to_timestamp = defaultdict(list)

    def set(self, *args):
        self.key_to_timestamp[args[0][0]].append((args[0][2], args[0][1]))

    # Do a binary search on sorted timestamps (log(N))
    def get(self, *args):
        possible_answers = self.key_to_timestamp.get(args[0][0], None)
        if possible_answers is None:
            return ''
        idx = bisect(possible_answers, (args[0][1], ord('z') + 1))
        return possible_answers[idx-1][1] if idx else ''


def create_time_map(queries, parameters):
    query_to_parameters = dict(zip(queries, parameters))
    time_map = None
    for query in query_to_parameters.keys():
        if query == 'TimeMap':
            time_map = TimeMap()
            continue
        if time_map is not None:
            getattr(time_map, query)(query_to_parameters[query])


if __name__ == '__main__':
    print(create_time_map(["TimeMap","set","get","get","set","get","get"],
                    [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]))
