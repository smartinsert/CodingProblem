"""
Given nxn board place n queen on this board so that they dont attack each other.
"""

from typing import List


class Position:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    def __str__(self):
        return f'({self.row}, {self.column})'


class SolveBoard:
    def __init__(self, number_of_squares: int):
        self.number_of_squares = number_of_squares
        self.positions = [Position] * number_of_squares

    def solve_n_queen_positions(self) -> List[Position]:
        has_solution = self.solve_n_queen_positions_util(0)
        return self.positions if has_solution else []

    def solve_n_queen_positions_util(self, row) -> bool:
        if self.number_of_squares == row:
            return True
        for column in range(self.number_of_squares):
            found_safe = True
            for queen in range(row):
                if self.positions[queen].column == column or self.positions[queen].row == row or \
                        self.positions[queen].column + self.positions[queen].row == row + column or \
                        self.positions[queen].row - self.positions[queen].column == row - column:
                    found_safe = False
                    break
            if found_safe:
                self.positions[row] = Position(row, column)
                if self.solve_n_queen_positions_util(row + 1):
                    return True
        return False


if __name__ == '__main__':
    n_queen_solver = SolveBoard(8)
    print([str(position) for position in n_queen_solver.solve_n_queen_positions()])
