def group_anagrams(strings):
    pairs = [(s, sorted(s)) for s in strings]
    pairs.sort(key=lambda p: p[1])
    return [p[0] for p in pairs]


if __name__ == "__main__":
    strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
    assert group_anagrams(strings) == ["bat", "tab", "car", "cat", "arts", "star", "rat", "tar"]
