class Solution(object):
    def maximumScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        if n ==1 :
            return 0

        dp = [[(0,0) for _ in range(n)] for _ in range(n+1)]
        for j in range(1, n):
                for i in range(n+ 1):
                    dp0, dp1 = dp[i][j-1]
                    prev = 0
                    curr = sum(grid[p][j] for p in range(i))

                    for k in range(n+1):
                        if k > 0 and k <= i: curr -= grid[k- 1][j]
                        if k > i: prev += grid[k- 1][j- 1]

                        maxprev= max(dp1, dp0 + prev)
                        n0 = max(dp[k][j][0], maxprev)
                        n1 = max(dp[k][j][1], maxprev+ curr)
                        dp[k][j] = (n0, n1)

        return max(dp[i][-1][1 ] for i in range(n +1))