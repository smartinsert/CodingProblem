

def occurrences(source, to_find):
    start_indices = list()
    start_idx = 0
    end_idx = len(source)
    while start_idx < end_idx:
        curr_str = source[start_idx:start_idx+len(to_find)]
        if curr_str == to_find:
            start_indices.append(start_idx)
        start_idx += 1
    return start_indices


if __name__ == '__main__':
    assert occurrences('abracadabra', 'abr') == [0, 7]
    assert not occurrences("abracadabra", "xyz")
    assert occurrences("aaaa", "aa") == [0, 1, 2]