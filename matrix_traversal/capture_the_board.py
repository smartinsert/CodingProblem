"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not
 flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to
 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution:
    def solve(self, board: [[]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        visited = set()

        # visit the boundaries
        # i == 0
        for j in range(len(board[0]) - 1):
            self.capture(board, 0, j, visited)

        # i == len(grid) - 1
        for j in range(len(board[0]) - 1):
            self.capture(board, len(board) - 1, j, visited)

        # j == 0
        for i in range(len(board) - 1):
            self.capture(board, i, 0, visited)

        # j == len(grid[0]) - 1
        for i in range(len(board) - 1):
            self.capture(board, i, len(board[0]) - 1, visited)

        for i in range(len(board)):
            for j in range(len(board[0]) - 1):
                if (i, j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'

    def capture(self, board, row, col, visited):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == 'X' or (
                row, col) in visited:
            return
        visited.add((row, col))
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for x, y in directions:
            self.capture(board, row + x, col + y, visited)


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
solution = Solution()
solution.solve(board)
