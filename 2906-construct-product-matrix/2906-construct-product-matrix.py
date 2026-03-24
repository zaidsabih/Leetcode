class Solution(object):
    def constructProductMatrix(self, grid):
        n, m = len(grid), len(grid[0])
        A = [[1] * m for r in grid]
        pre, suf, mod = 1, 1, 12345
        for i in range(n):
            for j in range(m):
                A[i][j] = A[i][j] * pre % mod
                A[~i][~j] = A[~i][~j] * suf % mod
                pre = pre * grid[i][j] % mod
                suf = suf * grid[~i][~j] % mod
        return A