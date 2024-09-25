from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        # Helper function for DFS
        def dfs(r: int, c: int):
            # Check bounds and if the cell is 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark the cell as escaped
            board[r][c] = 'E'
            
            # Explore all four directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Start from the first and last column
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        # Start from the first and last row
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # Now, capture surrounded regions and revert escaped 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Capture surrounded 'O's
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # Revert escaped 'O's
