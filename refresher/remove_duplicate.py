
def remove_duplicates(target: str) -> int:
    unique_str = set(target)
    return len(target) - len(unique_str)


if __name__ == '__main__':
    assert remove_duplicates('AAABCCD') == 3