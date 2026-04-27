class Solution:
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    streetDirections = {
       1: [1, 3],
       2: [0, 2],
       3: [2, 3],
       4: [1, 2],
       5: [0, 3],
       6: [0, 1]
    }
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        def dfs(i, j, oppositeDirection):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] < 0:
                return
            v = grid[i][j]
            sd = Solution.streetDirections[v]
            direction = (oppositeDirection + 2) % 4
            if direction not in sd:
                return
            grid[i][j] = -v
            for d in sd:
                delta = Solution.directions[d]
                dfs(i+delta[0], j+delta[1], d)
        dfs(0, 0, 0)
        dfs(0, 0, 3)
        return grid[m-1][n-1] < 0