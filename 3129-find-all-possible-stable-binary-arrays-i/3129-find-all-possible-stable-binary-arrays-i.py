class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        dp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        
        for i in range(1, min(limit, zero)+1):
            dp[i][0][0] = 1
        
        for j in range(1, min(limit, one)+1):
            dp[0][j][1] = 1
        
        for i in range(zero+1):
            for j in range(one+1):
                
                if i > 0:
                    for k in range(1, min(limit, i)+1):
                        dp[i][j][0] = (dp[i][j][0] + dp[i-k][j][1]) % MOD
                
                if j > 0:
                    for k in range(1, min(limit, j)+1):
                        dp[i][j][1] = (dp[i][j][1] + dp[i][j-k][0]) % MOD
        
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD