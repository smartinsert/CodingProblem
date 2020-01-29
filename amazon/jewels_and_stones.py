

def jewels_and_stones(jewels: str, stones: str) -> int:
    stones_are_jewels = 0
    for stone in stones:
        if stone in jewels:
            stones_are_jewels += 1

    return stones_are_jewels


if __name__ == '__main__':
    assert jewels_and_stones('aA', 'aAAbbbb') == 3
    assert jewels_and_stones('z', 'ZZ') == 0