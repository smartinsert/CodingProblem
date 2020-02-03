"""
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.
"""

from typing import *


def end_reachable(stones: List[int]) -> bool:
    if not stones:
        return False
    for i in range(3, len(stones)):
        if stones[i] > stones[i-1] * 2:
            return False
    set_of_stones = {stone for stone in stones}
    last_stone = stones[-1]
    positions, jumps = [0], [0]
    while positions:
        current_position = positions.pop()
        current_jump = jumps.pop()
        for i in range(current_jump - 1, current_jump + 2):
            if i <= 0:
                continue
            next_position = current_position + i
            if next_position == last_stone:
                return True
            elif next_position in set_of_stones:
                positions.append(next_position)
                jumps.append(i)
    return False


if __name__ == '__main__':
    print(end_reachable([0,1,3,5,6,8,12,17]))
    print(end_reachable([0,1,2,3,4,8,9,11]))