from queue import Queue


def rec_rearrange(target_string, result=None):
    if len(target_string) <= 1:
        return target_string
    if not result:
        result = list()
    if target_string[0] == target_string[1]:
        result.append(target_string[0])
    return rec_rearrange(target_string[1:]) + (result.pop() if result else '')

def rearrange(target_string):
    character_to_frequency = dict()
    for i in target_string:
        if not character_to_frequency.get(i):
            character_to_frequency[i] = 1
        else:
            character_to_frequency[i] = character_to_frequency.get(i) + 1
    # most_repeated = max(character_to_frequency.values())
    # remaining_values = sum(character_to_frequency.values()) - most_repeated
    # if remaining_values < most_repeated - 1:
    #     return None
    character_to_frequency = {k:v for k, v in sorted(character_to_frequency.items(), key=lambda x: x[1], reverse=True)}
    q = Queue()
    for key in character_to_frequency.keys():
        q.put((key, character_to_frequency.get(key)))
    result = ''
    while not q.empty():
        item = q.get()
        result += item[0]
        item = (item[0], item[1] - 1)
        if item[1]:
            q.put(item)
    return result


from collections import Counter
from queue import Queue


def rearrange_1(string):
    c = Counter(string)
    sitems = sorted(c.items(), key=lambda x: x[1], reverse=True)

    strlen = len(string)
    if strlen % 2:
        if sitems[0][1] > (strlen // 2) + 1:
            return None
    else:
        if sitems[0][1] > (strlen // 2):
            return None

    q = Queue()
    for item in sitems:
        q.put(item)

    new_str = ""
    while not q.empty():
        item = q.get()
        new_str += item[0]
        item = (item[0], item[1] - 1)
        if item[1]:
            q.put(item)

    return new_str


if __name__ == '__main__':
    # print(rearrange('aabbb'))

    # print(rearrange('aba'))

    # assert rearrange_1('aaabc') == "abaca"
    # assert rearrange("aaabbc") == "abcaba"

    print(rec_rearrange('aaabbc'))