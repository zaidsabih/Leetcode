class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        prev = [[-10**15]*3 for _ in range(n)]
        
        for k in range(3):
            if coins[0][0] < 0 and k > 0:
                prev[0][k] = 0
            elif k == 0:
                prev[0][k] = coins[0][0]
        
        for j in range(1, n):
            val = coins[0][j]
            for k in range(3):
                if val >= 0:
                    prev[j][k] = prev[j-1][k] + val
                else:
                    prev[j][k] = prev[j-1][k] + val
                    if k > 0:
                        prev[j][k] = max(prev[j][k], prev[j-1][k-1])
        
        for i in range(1, m):
            curr = [[-10**15]*3 for _ in range(n)]
            val = coins[i][0]
            
            for k in range(3):
                if val >= 0:
                    curr[0][k] = prev[0][k] + val
                else:
                    curr[0][k] = prev[0][k] + val
                    if k > 0:
                        curr[0][k] = max(curr[0][k], prev[0][k-1])
            
            for j in range(1, n):
                val = coins[i][j]
                for k in range(3):
                    best = max(prev[j][k], curr[j-1][k]) + val
                    if val < 0 and k > 0:
                        best = max(best, prev[j][k-1], curr[j-1][k-1])
                    curr[j][k] = best
            
            prev = curr
        
        return max(prev[n-1])