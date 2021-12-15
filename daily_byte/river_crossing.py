"""
A frog is attempting to cross a river to reach the other side. Within the river, there are stones located at different positions given by a stones array (this array is in sorted order). Starting on the first stone (i.e. stones[0]), the frog makes a jump of size one potentially landing on the next stone. If the frog’s last jump was of size x, the frog’s next jump may be of size x - 1, x, or x + 1. Given these following conditions return whether or not the frog can reach the other side.
Note: The frog may only jump in the forward direction.

Ex: Given the following stones…

stones = [0, 1, 10], return false.
This question is asked by Amazon. The frog can jump from stone 0 to stone 1, but then the gap is too far to jump to the last stone (i.e. the stone at position 10)
Ex: Given the following stones…

stones = [0, 1, 2, 4], return true.
The frog can jump from stone 0, to stone 1, to stone 2, to stone 4.
"""


def can_cross_the_river(stones: []) -> bool:
    if not stones or (len(stones) == 2 and stones[1] == 0):
        return False
    unique_jump_size = set(stones)
    return can_cross(stones, unique_jump_size, 1, 1)


def can_cross(stones: [], unique_jump_size: [], current_position: int, last_jump_size: int) -> bool:
    if current_position > stones[-1] or current_position not in unique_jump_size or last_jump_size == 0:
        return False
    if current_position == stones[-1]:
        return True
    return can_cross(stones, unique_jump_size, current_position + last_jump_size - 1, last_jump_size - 1) or \
           can_cross(stones, unique_jump_size, current_position + last_jump_size, last_jump_size) or \
           can_cross(stones, unique_jump_size, current_position + last_jump_size + 1, last_jump_size + 1)


print(can_cross_the_river([0, 1, 10]))
print(can_cross_the_river([0, 1, 2, 4]))
