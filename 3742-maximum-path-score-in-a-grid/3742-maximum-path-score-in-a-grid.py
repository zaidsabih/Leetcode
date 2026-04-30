
class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid:
            return -1
    
        n, m = len(grid), len(grid[0])
    
        memo={}
        def dfs(r, c, cost):
            # Out of bounds
            if r >= n or c >= m:
                return float("-inf")
            
            # Calculate new cost and score for this cell
            val = grid[r][c]
            add_score = val if val > 0 else 0
            add_cost = 1 if val in (1, 2) else 0
    
            cost += add_cost
    
            # If we exceed k, invalid path
            if cost > k:
                return float("-inf")
    
            # If reached destination
            if r == n - 1 and c == m - 1:
                return add_score if cost <= k else float("-inf")

            # Check memo
            key = (r, c, cost)
            if key in memo:
                return memo[key]
    
            # Explore right and down
            right = dfs(r, c + 1, cost)
            down = dfs(r + 1, c, cost)
    
            memo[key] = add_score + max(right, down)
            return memo[key]
    
        ans = dfs(0, 0, 0)
        return ans if ans != float("-inf") else -1