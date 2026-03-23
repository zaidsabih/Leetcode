class Solution:
    def maxProductPath(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # Initialize DP arrays
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        # First column
        for i in range(1, m):
            max_dp[i][0] = max_dp[i-1][0] * grid[i][0]
            min_dp[i][0] = max_dp[i][0]
        
        # First row
        for j in range(1, n):
            max_dp[0][j] = max_dp[0][j-1] * grid[0][j]
            min_dp[0][j] = max_dp[0][j]
        
        # Fill DP
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                
                candidates = [
                    max_dp[i-1][j] * val,
                    min_dp[i-1][j] * val,
                    max_dp[i][j-1] * val,
                    min_dp[i][j-1] * val
                ]
                
                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)
        
        result = max_dp[m-1][n-1]
        
        return result % MOD if result >= 0 else -1