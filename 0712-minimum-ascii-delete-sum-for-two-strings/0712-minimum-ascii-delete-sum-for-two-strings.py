class Solution:
    def minimumDeleteSum(self, s1, s2):
        if len(s2) > len(s1):
            s1, s2 = s2, s1

        n, m = len(s1), len(s2)

        dp = [0]*(m+1)

        for j in range(1, m+1):
            dp[j] = dp[j-1] + ord(s2[j-1])
        
        for i in range(1, n+1):
            prev_diag = dp[0]
            dp[0] += ord(s1[i-1])

            for j in range(1, m+1):

                temp = dp[j]

                if s1[i-1] == s2[j-1]:
                    dp[j] = prev_diag
                else:
                    dp[j] = min(
                        dp[j-1]+ord(s2[j-1]),
                        temp+ord(s1[i-1])
                    )
                prev_diag = temp

        return dp[m]