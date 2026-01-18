class Solution:
    def largestMagicSquare(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        min_size = min(rows, cols)  # Maximum possible square size

        for size in range(min_size, 1, -1):
            for r in range(rows - size + 1):
                for c in range(cols - size + 1):
                    if self.isMagic(grid, r, c, size):
                        return size      # break immediately when found

        return 1  # If no larger magic square found, smallest is 1

    def isMagic(self, grid, r, c, size):
        targetSum = 0

        # Sum of first row
        for j in range(size):
            targetSum += grid[r][c + j]

        # --- CHECK DIAGONALS FIRST ---
        diag1 = diag2 = 0
        for i in range(size):
            diag1 += grid[r + i][c + i]             # Main diagonal
            diag2 += grid[r + i][c + size - 1 - i]  # Anti-diagonal
        if diag1 != targetSum or diag2 != targetSum:
            return False

        # --- THEN CHECK ROWS ---
        for i in range(1, size):  # Skip first row, already used for targetSum
            s = 0
            for j in range(size):
                s += grid[r + i][c + j]
            if s != targetSum:
                return False

        # --- THEN CHECK COLUMNS ---
        for j in range(size):
            s = 0
            for i in range(size):
                s += grid[r + i][c + j]
            if s != targetSum:
                return False

        return True