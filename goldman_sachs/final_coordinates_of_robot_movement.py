"""
A robot can only move in four directions , UP(U), DOWN(D),LEFT(L),RIGHT(R).
Given a string consisting of instructions to move , output the co-ordinates of robot after the executing
the instructions. Initial position of robot is at origin(0,0)
"""

from typing import Tuple


def final_coordinates(movements: str) -> Tuple[int, int]:
    up_down_moves, left_right_moves = 0, 0
    for movement in movements:
        if movement == 'U':
            up_down_moves += 1
        elif movement == 'D':
            up_down_moves -= 1
        elif movement == 'L':
            left_right_moves -= 1
        elif movement == 'R':
            left_right_moves += 1
    return tuple((left_right_moves, up_down_moves))


if __name__ == '__main__':
    print(final_coordinates('UUUDULR'))
    print(final_coordinates(''))