class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        top, bottom = x, x + k - 1
        while top < bottom:
            for j in range(y, y + k):
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
            top += 1
            bottom -= 1
        return grid